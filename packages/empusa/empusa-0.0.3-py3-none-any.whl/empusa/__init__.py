import argparse
import json
import logging
import os
import re
import sys
import time

import click
import etcd
import tabulate

from typing import cast, Any, Dict, List, Optional, Tuple, Union


DEFAULT_ETCD_PROTOCOL = 'http'

SWITCH_ENABLED = ('yes', 'true', 'y', 'on', '1', 'enabled')
SWITCH_DISABLED = ('no', 'false', 'n', 'off', '0', 'disabled')
SWITCH_VALUES = SWITCH_ENABLED + SWITCH_DISABLED


def parse_endpoints(endpoint_specs: Union[str, List[str]]) -> List[Tuple[str, int]]:
    endpoints: List[Tuple[str, int]] = []

    if isinstance(endpoint_specs, str):
        endpoint_specs = [endpoint_specs]

    for item in endpoint_specs:
        for endpoint in item.split(','):
            try:
                host, port = endpoint.split(':')

            except ValueError:
                raise Exception('Endpoint "{}" is not in HOST:PORT format'.format(endpoint))

            endpoints += [
                (host.strip(), int(port.strip()))
            ]

    return endpoints


class EtcdClient:
    def __init__(
        self,
        tree: str,
        client_args: Optional[Any] = None,
        client_kwargs: Optional[Dict[str, Any]] = None,
        ttl: Optional[int] = None
    ) -> None:
        self._tree = tree
        self._ttl = ttl

        self._client_args = client_args or tuple()
        self._client_kwargs = client_kwargs or dict()

    @property
    def _client(self) -> etcd.Client:
        return etcd.Client(*self._client_args, **self._client_kwargs)

    def list_entities(
        self,
        entity_type: str,
        entity_subtype: Optional[str] = None
    ) -> List[etcd.EtcdResult]:
        if entity_subtype:
            key = '{self._tree}/{entity_type}/{entity_subtype}'.format(**locals())

        else:
            key = '{self._tree}/{entity_type}'.format(**locals())

        try:
            directory = self._client.read(key, recursive=True)

        except etcd.EtcdKeyNotFound:
            return []

        return [r for r in directory.children]

    def list_services(self, service_type: Optional[str] = None) -> List[Tuple[str, str, Optional[int]]]:
        return [
            (
                re.sub(r'^{}/service/(.*)'.format(self._tree), r'\1', service.key),
                service.value,
                service.ttl
            )
            for service in self.list_entities('service', entity_subtype=service_type)
        ]

    def list_switches(self) -> List[Tuple[str, str, Optional[int]]]:
        return [
            (
                re.sub(r'^{}/switch/(.*)'.format(self._tree), r'\1', switch.key),
                switch.value,
                switch.ttl
            )
            for switch in self.list_entities('switch')
        ]

    def register_entity(
        self,
        entity_type: str,
        name: str,
        value: Any,
        entity_subtype: Optional[str] = None,
        ttl: Optional[int] = None
    ) -> None:
        if entity_subtype:
            key = '{self._tree}/{entity_type}/{entity_subtype}/{name}'.format(**locals())

        else:
            key = key = '{self._tree}/{entity_type}/{name}'.format(**locals())

        self._client.write(
            key,
            value,
            ttl=ttl or self._ttl
        )

    def unregister_entity(
        self,
        entity_type: str,
        name: str,
        entity_subtype: Optional[str] = None,
    ) -> None:
        if entity_subtype:
            key = '{self._tree}/{entity_type}/{entity_subtype}/{name}'.format(**locals())

        else:
            key = '{self._tree}/{entity_type}/{name}'.format(**locals())

        try:
            self._client.delete(key)

        except etcd.EtcdKeyNotFound:
            logging.getLogger().info('{entity_type} {entity_subtype} {name} already unregistered'.format(**locals()))
            return

    def register_service(
        self,
        service_type: str,
        name: str,
        value: Any,
        ttl: Optional[int] = None
    ) -> None:
        self.register_entity('service', name, value, entity_subtype=service_type, ttl=ttl)

        logging.getLogger().info('service {name} ({service_type}) registered'.format(**locals()))

    def unregister_service(
        self,
        service_type: str,
        name: str
    ) -> None:
        self.unregister_entity('service', name, entity_subtype=service_type)

        logging.getLogger().info('service {name} ({service_type}) unregistered'.format(**locals()))

    def get_switch(
        self,
        name: str
    ) -> Optional[str]:
        key = '{self._tree}/switch/{name}'.format(**locals())

        try:
            result = self._client.get(key)

        except etcd.EtcdKeyNotFound:
            return None

        else:
            return cast(str, result.value)

    def set_switch(
        self,
        name: str,
        value: Any,
        ttl: Optional[int] = None
    ) -> None:
        self.register_entity('switch', name, value, ttl=ttl)

        logging.getLogger().info('switch {name} set to {value}'.format(**locals()))

    def toggle_switch(
        self,
        name: str,
    ) -> None:
        key = '{self._tree}/switch/{name}'.format(**locals())

        try:
            result = self._client.get(key)

        except etcd.EtcdKeyNotFound:
            logging.getLogger().error('switch {name} not set'.format(**locals()))

            sys.exit(1)

        current_value = result.value
        normalized_current_value = current_value.strip().lower()

        if normalized_current_value not in SWITCH_VALUES:
            logging.getLogger().error('switch {name} does not have boolean value'.format(**locals()))

            sys.exit(1)

        if normalized_current_value in SWITCH_ENABLED:
            value = 'no'

        else:
            value = 'yes'

        try:
            self._client.test_and_set(key, value, current_value)

        except ValueError:
            logging.getLogger().warn('switch {name} already toggled'.format(**locals()))

        else:
            logging.getLogger().info('switch {name} set to {value}'.format(**locals()))

    def remove_switch(
        self,
        name: str
    ) -> None:
        self.unregister_entity('switch', name)

        logging.getLogger().info('switch {name} removed'.format(**locals()))


@click.group()
@click.pass_context
@click.option(
    '--etcd-endpoint',
    type=str, envvar='EMPUSA_ETCD_ENDPOINT',
    required=True, metavar='HOST:PORT', multiple=True
)
@click.option(
    '--etcd-protocol',
    type=str, envvar='EMPUSA_ETCD_PROTOCOL',
    default=DEFAULT_ETCD_PROTOCOL
)
@click.option(
    '--tree-root',
    type=str, envvar='EMPUSA_TREE_ROOT',
    required=True
)
@click.option(
    '--ca-bundle',
    type=str, envvar='EMPUSA_CA_BUNDLE',
    default=None
)
def cmd_root(
    ctx: Any,
    etcd_endpoint: List[str],
    etcd_protocol: str,
    tree_root: str,
    ca_bundle: Optional[str]
) -> None:
    ctx.ensure_object(argparse.Namespace)
    cfg = ctx.obj

    endpoints = parse_endpoints(etcd_endpoint)

    if not endpoints:
        raise Exception('At least one etcd endpoint must be specified')

    endpoint = endpoints[0]

    if ca_bundle is None:
        # For better compatibility with the outer world, accept also REQUESTS_CA_BUNDLE envvar.
        ca_bundle = os.getenv('REQUESTS_CA_BUNDLE', None)

    cfg.client = EtcdClient(
        tree_root,
        client_kwargs={
            'host': endpoint[0],
            'port': endpoint[1],
            'protocol': etcd_protocol,
            'allow_reconnect': False,
            'ca_cert': ca_bundle
        }
    )


@cmd_root.group(name='service')
def cmd_service() -> None:
    pass


@cmd_service.command(name='list')
@click.option('--service-type', type=str, envvar='EMPUSA_SERVICE_TYPE', default=None)
@click.option('--format', type=click.Choice(['table', 'json']), default='table')
@click.pass_obj
def cmd_service_list(
    cfg: Any,
    service_type: Optional[str],
    format: str
) -> None:
    services = sorted(
        cfg.client.list_services(service_type=service_type),
        key=lambda x: x[0]
    )

    if format == 'table':
        table = [
            [
                'Service', 'Location', 'TTL'
            ]
        ]

        for name, value, ttl in services:
            table += [
                [
                    name,
                    value,
                    ttl
                ]
            ]

        print(tabulate.tabulate(table, tablefmt='psql', headers='firstrow'))

    elif format == 'json':
        print(json.dumps([
            {
                'service': name,
                'location': value,
                'ttl': ttl
            }
            for name, value, ttl in services
        ]))


@cmd_service.command(name='register')
@click.option('--service-type', type=str, envvar='EMPUSA_SERVICE_TYPE', required=True)
@click.option('--service-name', type=str, envvar='EMPUSA_SERVICE_NAME', required=True)
@click.option('--service-location', type=str, envvar='EMPUSA_SERVICE_LOCATION', required=True)
@click.option('--ttl', type=int, envvar='EMPUSA_SERVICE_TTL')
@click.option('--refresh-every', type=int, envvar='EMPUSA_SERVICE_REFRESH_EVERY')
@click.pass_obj
def cmd_service_register(
    cfg: Any,
    service_type: str,
    service_name: str,
    service_location: str,
    ttl: Optional[int] = None,
    refresh_every: Optional[int] = None
) -> None:
    def _register() -> None:
        cfg.client.register_service(
            service_type,
            service_name,
            service_location,
            ttl=ttl
        )

    if not refresh_every:
        _register()
        return

    while True:
        _register()

        time.sleep(refresh_every)


@cmd_service.command(name='unregister')
@click.option('--service-type', type=str, envvar='EMPUSA_SERVICE_TYPE', required=True)
@click.option('--service-name', type=str, envvar='EMPUSA_SERVICE_NAME', required=True)
@click.pass_obj
def cmd_service_unregister(
    cfg: Any,
    service_type: str,
    service_name: str
) -> None:
    cfg.client.unregister_service(
        service_type,
        service_name
    )


@cmd_root.group(name='switch')
def cmd_switch() -> None:
    pass


@cmd_switch.command(name='list')
@click.option('--format', type=click.Choice(['table', 'json']), default='table')
@click.pass_obj
def cmd_switch_list(
    cfg: Any,
    format: str
) -> None:
    switches = sorted(
        cfg.client.list_switches(),
        key=lambda x: x[0]
    )

    if format == 'table':
        table = [
            [
                'Switch', 'Value', 'TTL'
            ]
        ]

        for name, value, ttl in switches:
            table += [
                [
                    name,
                    value,
                    ttl
                ]
            ]

        print(tabulate.tabulate(table, tablefmt='psql', headers='firstrow'))

    elif format == 'json':
        print(json.dumps([
            {
                'switch': name,
                'value': value,
                'ttl': ttl
            }
            for name, value, ttl in switches
        ]))


@cmd_switch.command(name='set')
@click.argument('switch', metavar='SWITCH', nargs=1)
@click.argument('value', metavar='VALUE', nargs=1)
@click.pass_obj
def cmd_switch_set(
    cfg: Any,
    switch: str,
    value: str
) -> None:
    cfg.client.set_switch(
        switch,
        value
    )


@cmd_switch.command(name='toggle')
@click.argument('switch', metavar='SWITCH', nargs=1)
@click.pass_obj
def cmd_switch_toggle(
    cfg: Any,
    switch: str
) -> None:
    cfg.client.toggle_switch(
        switch
    )


@cmd_switch.command(name='get')
@click.argument('switch', metavar='SWITCH', nargs=1)
@click.pass_obj
def cmd_switch_get(
    cfg: Any,
    switch: str
) -> None:
    value = cfg.client.get_switch(switch)

    if value is None:
        print('No such switch "{}"'.format(switch))
        sys.exit(1)

    print(value)


@cmd_switch.command(name='remove')
@click.argument('switch', metavar='SWITCH', nargs=1)
@click.pass_obj
def cmd_switch_remove(
    cfg: Any,
    switch: str
) -> None:
    cfg.client.remove_switch(switch)


def main() -> None:
    logging.basicConfig(
        level=logging._nameToLevel[os.environ.get('EMPUSA_LOGLEVEL', 'INFO').upper()]
    )

    cmd_root()


if __name__ == '__main__':
    main()
