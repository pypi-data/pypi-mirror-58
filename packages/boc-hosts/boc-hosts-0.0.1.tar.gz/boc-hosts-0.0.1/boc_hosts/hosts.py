"""
BitOfCode Hosts module
"""
import copy
import os
import yaml
import re

FORMAT_YAML = 'YAML'


class Hosts:
    """
    Manages the hosts file
    """

    def __init__(self) -> None:
        super().__init__()
        self._entries = dict()

    def update(self, ip_address, *host_name):
        """
        Update an existing host-ip entry or inserting a new entry if it doesn't exists yet.
        :param ip_address:
        :param host_name:
        """
        hosts = self._entries.get(f"{ip_address}", set())
        for host in host_name:
            hosts.add(f"{host}")
        self._entries[f"{ip_address}"] = hosts

    def get_hosts(self, ip_address):
        """
        Returns a set of hosts which points tp the given ip_address
        :param ip_address: the ip_address which the hosts points to.
        :return: set of hosts which points to the provided ip_address or empty-set.
        """
        return set(self._entries.get(f"{ip_address}", set()))

    def remove_host_name(self, host):
        """
        removes the host-name
        :param host: the host-name to be removed
        """
        host_name = f"{host}"

        for ip_address, hosts in self._entries.items():
            if host_name in hosts:
                hosts.remove(host_name)
                self._entries[ip_address] = hosts

    def entries(self):
        deepcopy = copy.deepcopy(self._entries)
        for k, v in deepcopy.items():
            deepcopy[k] = list(v)
        return deepcopy


def serialize(hosts: Hosts):
    """
    returns a dictionary containing the hosts-model
    """
    entries = hosts.entries()
    for k, v in entries.items():
        entries[k] = list(v)
    return copy.deepcopy(entries)


def deserialize(serialized: dict) -> Hosts:
    """
    deserializes the result of :func:serialize(hosts)
    :param serialized: the serialized hosts
    :return: hosts of type :class:Hosts
    """
    hosts = Hosts()
    for ip_address, host_names in serialized.items():
        if type(host_names) is str:
            hosts.update(ip_address, host_names)
        else:
            hosts.update(ip_address, *host_names)
    return hosts


def write_hosts(hosts: Hosts, write):
    """
    Write the hosts-model into a hosts-file
    :param hosts: the hosts-model
    :param write: to write to
    """
    entries = hosts.entries()
    for ip_address, host_names in entries.items():
        for host_name in host_names:
            write(f"{ip_address}  {host_name}{os.linesep}")


def _write_config_yaml(data, stream):
    yaml.dump(data, stream)


def _read_config_yaml(stream, loader=yaml.FullLoader):
    return yaml.load(stream, Loader=loader)


writers = {
    FORMAT_YAML: _write_config_yaml
}

readers = {
    FORMAT_YAML: _read_config_yaml
}


def write_config_file(hosts: Hosts, path, output_format=FORMAT_YAML):
    writer = writers.get(output_format, None)
    if writer is not None:
        with open(path, 'w') as file:
            writer(serialize(hosts), file)


def read_config_file(out_file_yml) -> Hosts:
    _, extension = os.path.splitext(out_file_yml)
    reader = None
    if f"{extension}".upper() in ['.YML', '.YAML']:
        reader = readers.get(FORMAT_YAML)

    if reader is None:
        raise Exception(f"{extension} is not supported of '{out_file_yml}'")

    with open(out_file_yml, 'r') as file:
        data = reader(file)
        return deserialize(data)


def read_hosts(out_file_hosts) -> Hosts:
    host = Hosts()
    with open(out_file_hosts, 'r') as f:
        for line in f:
            hosts_line = line.strip()
            if hosts_line.startswith("#"):
                pass
            else:
                split = re.split(r'#', hosts_line)
                comment = split[0]
                line = re.split(r'\s+', comment)
                striped = map(lambda x: x.strip(), line)
                filtered = filter(lambda x: not x.startswith("#") and '' != x, striped)
                cleaned_line = list(filtered)
                if len(cleaned_line) >= 2:
                    for h in cleaned_line[1:]:
                        host.update(cleaned_line[0], h)
    return host
