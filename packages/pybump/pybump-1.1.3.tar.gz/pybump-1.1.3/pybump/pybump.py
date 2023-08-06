import argparse
import os
import re

import yaml
from pkg_resources import get_distribution, DistributionNotFound

regex_version_pattern = re.compile(r"((?:__)?version(?:__)? ?= ?[\"'])(.+?)([\"'])")


def is_valid_helm_chart(content):
    """
    Check if input dictionary contains mandatory keys of a Helm Chart.yaml file
    :param content: parsed YAML file as dictionary of key values
    :return: True if dict contains mandatory values, else False
    """
    return all(x in content for x in ['apiVersion', 'appVersion', 'description', 'name', 'version'])


def get_setup_py_version(content):
    """
    Extract 'version' value using regex from 'content'
    :param content: the content of a setup.py file
    :return: version value as string
    """
    version_match = regex_version_pattern.findall(content)
    if len(version_match) > 1:
        raise RuntimeError("More than one 'version' found: {0}".format(version_match))
    if not version_match:
        raise RuntimeError("Unable to find version string in: {0}".format(content))
    return version_match[0][1]


def set_setup_py_version(version, content):
    """
    Replace version in setup.py file using regex,
    g<1> contains the string left of version
    g<3> contains the string right of version
    :param version: string
    :param content: content of setup.py as string
    :return: content of setup.py file with 'version'
    """
    return regex_version_pattern.sub('\g<1>{}\g<3>'.format(version), content)


def is_semantic_string(semantic_string):
    """
    Check if input string is a semantic version as defined here: https://github.com/semver/semver/blob/master/semver.md,
    The version is allowed a lower case 'v' character.
    Function will search a match according to the regular expresion, so for example '1.1.2-prerelease+meta' is valid,
    then make sure there is and exact singe match and validate if each of x,y,z is an integer.
    return {'prefix': boolean, 'version': [x, y, z], 'release': 'some-release', 'metadata': 'some-metadata'} if True

    :param semantic_string: string
    :return: dict if True, else False
    """
    if type(semantic_string) != str or len(semantic_string) == 0:
        return False

    version_prefix = False
    # In case the version if of type 'v2.2.5' then save 'v' prefix and cut it for further 'semver' validation
    if semantic_string[0] == 'v':
        semantic_string = semantic_string[1:]
        version_prefix = True

    semver_regex = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"  # Match x.y.z
                              # Match -sometext-12.here
                              r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
                              r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
                              # Match +more.123.here
                              r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")
    # returns a list of tuples, for example [('2', '2', '7', 'alpha', '')]
    match = semver_regex.findall(semantic_string)

    # There was no match using 'semver_regex', since if 0 or more then single match found and empty list returned
    if len(match) == 0:
        return False

    try:
        semantic_array = [int(n) for n in match[0][:3]]
    except ValueError:
        return False

    return {'prefix': version_prefix, 'version': semantic_array, 'release': match[0][3], 'metadata': match[0][4]}


def bump_version(version_array, level):
    """
    Perform ++1 action on the array [x, y, z] cell,
    Input values are assumed to be validated
    :param version_array: int array of [x, y, z] validated array
    :param level: string represents major|minor|patch
    :return: int array with new value
    """
    if type(version_array) != list:
        raise ValueError("Error, invalid version_array: '{}', "
                         "should be [x, y, z].".format(version_array))

    if level == 'major':
        version_array[0] += 1
        version_array[1] = 0
        version_array[2] = 0
    elif level == 'minor':
        version_array[1] += 1
        version_array[2] = 0
    elif level == 'patch':
        version_array[2] += 1
    else:
        raise ValueError("Error, invalid level: '{}', "
                         "should be major|minor|patch.".format(level))

    return version_array


def get_self_version(dist_name):
    """
    Return version number of input distribution name,
    If distribution not found return not found indication
    :param dist_name: string
    :return: version as string
    """
    try:
        return get_distribution(dist_name).version
    except DistributionNotFound:
        return 'version not found'


def assemble_version_string(prefix, version_array, release, metadata):
    """
    reconstruct version
    :param prefix: boolean
    :param version_array: list of ints
    :param release: string
    :param metadata: sting
    :return: string
    """
    result_string = ''
    if prefix:
        result_string = 'v'
    result_string += '.'.join(str(x) for x in version_array)
    if release:
        result_string += '-' + release

    if metadata:
        result_string += '+' + metadata

    return result_string


def main():
    parser = argparse.ArgumentParser(description='Python version bumper')
    subparsers = parser.add_subparsers(dest='sub_command')

    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(get_self_version('pybump')),
                        help='Print version and exit')

    # Define parses that is shared, and will be used as 'parent' parser to all others
    base_sub_parser = argparse.ArgumentParser(add_help=False)
    base_sub_parser.add_argument('--file', help='Path to Chart.yaml/setup.py/VERSION file', required=True)
    base_sub_parser.add_argument('--app-version', action='store_true',
                                 help='Bump Helm chart appVersion, relevant only for Chart.yaml files', required=False)

    # Sub-parser for bump version command
    parser_bump = subparsers.add_parser('bump', parents=[base_sub_parser])
    parser_bump.add_argument('--level', choices=['major', 'minor', 'patch'], help='major|minor|patch', required=True)
    parser_bump.add_argument('--quiet', action='store_true', help='Do not print new version', required=False)

    # Sub-parser for set version command
    parser_set = subparsers.add_parser('set', parents=[base_sub_parser])
    parser_set.add_argument('--set-version',
                            help='Semantic version to set as a combination of \'vX.Y.Z-release+metadata\'',
                            required=True)
    parser_set.add_argument('--quiet', action='store_true', help='Do not print new version', required=False)

    # Sub-parser for get version command
    parser_get = subparsers.add_parser('get', parents=[base_sub_parser])
    parser_get.add_argument('--sem-ver', action='store_true', help='Get the main version only', required=False)
    parser_get.add_argument('--release', action='store_true', help='Get the version release only', required=False)
    parser_get.add_argument('--metadata', action='store_true', help='Get the version metadata only', required=False)

    args = vars(parser.parse_args())

    # Case where no args passed, sub_command is mandatory
    if args['sub_command'] is None:
        parser.print_help()
        exit(0)

    current_version = ""
    setup_py_content = ""
    chart_yaml = {}

    with open(args['file'], 'r') as stream:
        filename, file_extension = os.path.splitext(args['file'])

        if file_extension == '.py':
            setup_py_content = stream.read()
            current_version = get_setup_py_version(setup_py_content)
        elif file_extension == '.yaml' or file_extension == '.yml':
            try:
                chart_yaml = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

            if is_valid_helm_chart(chart_yaml):
                if args['app_version']:
                    current_version = chart_yaml['appVersion']
                else:
                    current_version = chart_yaml['version']
            else:
                raise ValueError("Input file is not a valid Helm chart.yaml: {0}".format(chart_yaml))
        else:
            if os.path.basename(filename) == 'VERSION':
                # A version file should ONLY contain a valid semantic version string
                current_version = stream.read()
            else:
                raise ValueError("File name or extension not known to this app: {}{}"
                                 .format(os.path.basename(filename), file_extension))

    current_version_dict = is_semantic_string(current_version)
    if not current_version_dict:
        print("Invalid semantic version format: {}".format(current_version))
        exit(1)

    if args['sub_command'] == 'get':
        if args['sem_ver']:
            # Join the array of current_version_dict by dots
            print('.'.join(str(x) for x in current_version_dict.get('version')))
        elif args['release']:
            print(current_version_dict.get('release'))
        elif args['metadata']:
            print(current_version_dict.get('metadata'))
        else:
            print(current_version)
    else:
        # Set the 'new_version' value
        if args['sub_command'] == 'set':
            set_version = args['set_version']
            if not is_semantic_string(set_version):
                print("Invalid semantic version format: {}".format(set_version))
                exit(1)
            new_version = set_version
        else:  # bump version ['sub_command'] == 'bump'
            # Only bump value of the 'version' key
            new_version_array = bump_version(current_version_dict.get('version'), args['level'])
            # Reconstruct new version with rest dict parts if exists
            new_version = assemble_version_string(prefix=current_version_dict.get('prefix'),
                                                  version_array=new_version_array,
                                                  release=current_version_dict.get('release'),
                                                  metadata=current_version_dict.get('metadata'))

        # Append the 'new_version' to relevant file
        with open(args['file'], 'w') as outfile:
            if file_extension == '.py':
                outfile.write(set_setup_py_version(new_version, setup_py_content))
            elif file_extension == '.yaml' or file_extension == '.yml':
                if args['app_version']:
                    chart_yaml['appVersion'] = new_version
                else:
                    chart_yaml['version'] = new_version
                yaml.dump(chart_yaml, outfile, default_flow_style=False)
            elif os.path.basename(filename) == 'VERSION':
                outfile.write(new_version)
            outfile.close()

        if args['quiet'] is False:
            print(new_version)


if __name__ == "__main__":
    main()
