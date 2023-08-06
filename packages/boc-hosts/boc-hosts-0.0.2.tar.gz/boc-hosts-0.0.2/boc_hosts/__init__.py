"""
The boc-hosts
"""

from .hosts import Hosts
from .hosts import serialize, deserialize, \
    write_config_file, read_config_file, \
    write_hosts, read_hosts
from .hosts import FORMAT_YAML
