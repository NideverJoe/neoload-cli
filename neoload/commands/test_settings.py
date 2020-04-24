import copy
import json
import sys

import click

from neoload_cli_lib import rest_crud
from neoload_cli_lib import tools
from neoload_cli_lib import user_data, cli_exception
from neoload_cli_lib.name_resolver import Resolver

__endpoint = "v2/tests"
__resolver = Resolver(__endpoint)

meta_key = 'settings id'


@click.command()
@click.argument('command', type=click.Choice(['ls', 'create', 'put', 'patch', 'delete', 'use'], case_sensitive=False),
                required=False)
@click.argument("name", type=str, required=False)
@click.option('--rename', help="rename test settings")
@click.option('--description', help="provide a description")
@click.option('--scenario', help="change the scenario of project")
@click.option('--zone', 'controller_zone_id', help="controller zone and it default zone for the lg.")
@click.option('--lgs', 'lg_zone_ids', help="precise how many lg and other zone if needed. by default we use one lg.")
@click.option('--naming-pattern', 'naming_pattern', help="")
def cli(command, name, rename, description, scenario, controller_zone_id, lg_zone_ids, naming_pattern):
    """create/read/update/delete test settings"""
    if not command:
        print("command is mandatory. Please see neoload tests-settings --help")
        return
    rest_crud.set_current_sub_command(command)
    if name == "cur":
        name = user_data.get_meta(meta_key)
    is_id = tools.is_id(name)
    # avoid to make two requests if we have not id.
    if command == "ls":
        tools.ls(name, is_id, __resolver)
        return
    elif command == "create":
        id_created = create(create_json(name, description, scenario, controller_zone_id, lg_zone_ids, naming_pattern))
        user_data.set_meta(meta_key, id_created)
        return

    __id = tools.get_id(name, __resolver, is_id)

    if command == "use":
        tools.use(__id, meta_key, __resolver)
        return

    if not __id:
        __id = user_data.get_meta_required(meta_key)

    if command == "put":
        put(__id, create_json(rename, description, scenario, controller_zone_id, lg_zone_ids, naming_pattern))
        user_data.set_meta(meta_key, __id)
    elif command == "patch":
        patch(__id, create_json(rename, description, scenario, controller_zone_id, lg_zone_ids, naming_pattern))
        user_data.set_meta(meta_key, __id)
    elif command == "delete":
        delete(__id)
        user_data.set_meta(meta_key, None)

def get_current_test_settings_json():
    return tools.get_named_or_id(user_data.get_meta(meta_key), True, __resolver)

def create(json_data):
    rep = rest_crud.post(__endpoint, fill_default_fields(json_data))
    return tools.get_id_and_print_json(rep)


def put(id_settings, json_data):
    rep = rest_crud.put(get_end_point(id_settings), fill_default_fields(json_data))
    tools.get_id_and_print_json(rep)


def patch(id_settings, json_data):
    rep = rest_crud.patch(get_end_point(id_settings), fill_default_fields(json_data))
    tools.get_id_and_print_json(rep)


def delete(__id):
    rep = tools.delete(__endpoint, __id, "settings")
    tools.print_json(rep.json())
    user_data.set_meta(meta_key, None)


def get_end_point(id_test: str):
    return __endpoint + "/" + id_test


def create_json(name, description, scenario, controller_zone_id, lg_zone_ids, naming_pattern):
    data = {}
    if name is not None:
        data['name'] = name
    if description is not None:
        data['description'] = description
    if scenario is not None:
        data['scenarioName'] = scenario
    if controller_zone_id is not None:
        data['controllerZoneId'] = controller_zone_id
    if lg_zone_ids is not None:
        data['lgZoneIds'] = parse_zone_ids(lg_zone_ids, controller_zone_id)
    if naming_pattern is not None:
        data['testResultNamingPattern'] = naming_pattern

    if len(data) == 0:
        data = manual_json(data)

    return data


def manual_json(data):
    if sys.stdin.isatty():
        for field in ['name', 'description', 'scenarioName', 'controllerZoneId', 'testResultNamingPattern']:
            data[field] = input(field)
        data['lgZoneIds'] = parse_zone_ids(input("lgZoneIds"), data['controllerZoneId'])
    else:
        try:
            data = json.loads(sys.stdin.read())
        except json.JSONDecodeError as err:
            raise cli_exception.CliException('%s\nThis command requires a valid Json input.\n'
                                             'Example: neoload test-settings create {"name":"TestName"}' % str(err))
    return data


def parse_zone_ids(lg_zone_ids, controller_zone):
    if tools.is_integer(lg_zone_ids):
        return {default_zone(controller_zone): int(lg_zone_ids)}
    values = {}
    for zone in lg_zone_ids.split(","):
        split = zone.split(":")
        values[split[0].strip()] = split[1].strip()
    return values


def default_zone(zone: str):
    return 'defaultzone' if zone is None or zone.strip() == '' else zone


def default_lgs(lg_zone_ids, controller_zone_id: str):
    if isinstance(lg_zone_ids, dict) and len(lg_zone_ids) > 0:
        return lg_zone_ids
    lgs = '1' if lg_zone_ids is None or lg_zone_ids == {} else lg_zone_ids
    if tools.is_integer(lgs):
        return parse_zone_ids(lgs, controller_zone_id)
    return parse_zone_ids(lg_zone_ids, controller_zone_id)


def fill_default_fields(json_data):
    data = copy.deepcopy(json_data)
    data.update([
        ('controllerZoneId', default_zone(json_data.get('controllerZoneId'))),
        ('lgZoneIds', default_lgs(json_data.get('lgZoneIds'), json_data.get('controllerZoneId')))
    ])
    return data
