"""
Faraday Penetration Test IDE
Copyright (C) 2013  Infobyte LLC (http://www.infobytesec.com/)
See the file 'doc/LICENSE' for the license information
"""
from faraday_plugins.plugins.plugin import PluginBase
import re
import os
import random

current_path = os.path.abspath(os.getcwd())

__author__ = "Francisco Amato"
__copyright__ = "Copyright (c) 2013, Infobyte LLC"
__credits__ = ["Francisco Amato"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Francisco Amato"
__email__ = "famato@infobytesec.com"
__status__ = "Development"


class HydraParser:
    """
    The objective of this class is to parse an xml file generated by the hydra tool.

    @param hydra_filepath A proper simple report generated by hydra
    """

    def __init__(self, xml_output):
        lines = xml_output.splitlines()
        self.items = []
        for l in lines:

            reg = re.search(
                "\[([^$]+)\]\[([^$]+)\] host: ([^$]+)   login: ([^$]+)   password: ([^$]+)",
                l)

            if reg:

                item = {
                    'port': reg.group(1),
                    'plugin': reg.group(2),
                    'ip': reg.group(3),
                    'login': reg.group(4),
                    'password': reg.group(5)}

                self.items.append(item)


class HydraPlugin(PluginBase):
    """
    Example plugin to parse hydra output.
    """

    def __init__(self):
        super().__init__()
        self.id = "Hydra"
        self.name = "Hydra XML Output Plugin"
        self.plugin_version = "0.0.1"
        self.version = "7.5"
        self.options = None
        self._current_output = None
        self._current_path = None
        self._command_regex = re.compile(
            r'^(sudo hydra|sudo \.\/hydra|hydra|\.\/hydra).*?')
        self.host = None


    def parseOutputString(self, output, debug=False):
        """
        This method will discard the output the shell sends, it will read it from
        the xml where it expects it to be present.

        NOTE: if 'debug' is true then it is being run from a test case and the
        output being sent is valid.
        """

        parser = HydraParser(output)

        i = 0
        hosts = {}
        service = ''
        port = ''

        for item in parser.items:

            service = item['plugin']
            port = item['port']

            if item['ip'] not in hosts:
                hosts[item['ip']] = []

            hosts[item['ip']].append([item['login'], item['password']])

        for k, v in hosts.items():

            h_id = self.createAndAddHost(k)

            if self._isIPV4(k):

                i_id = self.createAndAddInterface(
                    h_id,
                    k,
                    ipv4_address=k)

            else:
                i_id = self.createAndAddInterface(
                    h_id,
                    k,
                    ipv6_address=k)

            s_id = self.createAndAddServiceToInterface(
                h_id,
                i_id,
                service,
                ports=[port],
                protocol="tcp",
                status="open")

            for cred in v:
                self.createAndAddCredToService(
                    h_id,
                    s_id,
                    cred[0],
                    cred[1])

                self.createAndAddVulnToService(
                    h_id,
                    s_id,
                    "Weak Credentials",
                    "[hydra found the following credentials]\nuser:%s\npass:%s" % (cred[0], cred[1]),
                    severity="high")

        del parser

    xml_arg_re = re.compile(r"^.*(-o\s*[^\s]+).*$")

    def processCommandString(self, username, current_path, command_string):

        self._output_file_path = os.path.join(
            self.data_path,
            "hydra_output-%s.txt" % random.uniform(1, 10))

        arg_match = self.xml_arg_re.match(command_string)

        if arg_match is None:
            return re.sub(r"(^.*?hydra?)", r"\1 -o %s" % self._output_file_path, command_string)
        else:
            return re.sub(
                arg_match.group(1),
                r"-o %s" % self._output_file_path,
                command_string)

    def _isIPV4(self, ip):
        if len(ip.split(".")) == 4:
            return True
        else:
            return False

    def setHost(self):
        pass


def createPlugin():
    return HydraPlugin()

# I'm Py3
