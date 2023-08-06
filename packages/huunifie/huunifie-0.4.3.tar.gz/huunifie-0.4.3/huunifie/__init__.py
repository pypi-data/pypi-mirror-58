# coding=utf-8
"""
Licensed under WTFPL.
http://www.wtfpl.net/about/
"""
import argparse
import configparser
import json
import logging
import time
from datetime import datetime
from pathlib import Path

import requests
import urllib3
from pap_logger import *
from requests.exceptions import ConnectionError

__app_name__ = 'huunifie'
__version__ = '0.4'
__author__ = 'kurisuD'

__desc__ = """A Hue bridge and Unifi controller client.
Enables/disables specified Hue schedules in the presence/absence of specified wifi devices on the Unifi controller."""

__interval__ = 3
__config_path__ = Path("~/.huunifie.conf").expanduser()

__unifi_controller_host__ = "localhost"
__unifi_controller_port__ = 8443
__unifi_controller_user__ = "hue"
__unifi_controller_pwd__ = "hue_password!!"

__unifi_api_login__ = "/api/login"
__unifi_api_clients_stats__ = "/api/s/default/stat/sta"

__hue_hub_host__ = "hue"
__hue_hub_port__ = 80
__hue_key__ = "Your_40_alphanumeric_hue_api_key_please."

__zmq_default_publishing_host__ = "*"
__zmq_default_publishing_port__ = 12168  # hu = 104*117

__wifi_clients_example__ = ["01:23:45:67:89:ab", "your_device_hostname"]
__schedules_names_example__ = ["A schedule name with spaces", "another_without"]


class ZmqPublisher:
    """
    Sends client info via zmq
    """

    def __init__(self, args):
        if "no_pub" in args and args.no_pub:
            logging.error("ZMQ publication is disabled.")
            self.available = False
            return
        try:
            import zmq
            context = zmq.Context()
            self._socket = context.socket(zmq.PUB)
            self._socket.setsockopt(zmq.CONFLATE, 1)
            self._socket.bind("tcp://{}:{}".format(args.pub_host, args.pub_port))
            logging.info("ZMQ publication available on port {}".format(args.pub_port))
            self.available = True
        except ImportError:
            logging.error("zmq module is not available.")
            self.available = False

    def send_client_info(self, clients_info: list):
        """
        publishes the (watched) connected clients info
        :param clients_info: a list of dictionaries
        """
        self._socket.send_string(json.dumps(clients_info))


class HueClient:
    """
    Connects to the Hue hub, enables or disables the schedules.
    """

    def __init__(self, args):
        for mandatory_value in ["hue_host", "hue_port", "hue_key"]:
            if mandatory_value not in args or vars(args)[mandatory_value] is None:
                raise ValueError("{} not specified in the config file nor on the command line.".format(mandatory_value))

        self._url_prefix = "http://{}:{}/api/{}".format(args.hue_host, args.hue_port, args.hue_key)
        self._schedules_names = args.schedules_names

    def change_schedules(self, enabled=False):
        """
        Connects to the Hue hub, enable or disable the schedules.
        """
        status = "enabled" if enabled else "disabled"
        url = "{}/schedules".format(self._url_prefix)
        try:
            schedules_raw = requests.get(url)
            if isinstance(schedules_raw.content, bytes):
                schedules_raw_content = schedules_raw.content.decode()
            else:
                schedules_raw_content = schedules_raw.content

            if schedules_raw.ok:
                content = json.loads(schedules_raw_content)
                if isinstance(content, list) and "error" in content[0]:
                    msg = "Error accessing schedules : {}".format(content[0]["error"]["description"])
                    logging.error(msg)
                    raise PermissionError(msg)
                for schedule_id, schedule in content.items():
                    if schedule["name"] in self._schedules_names:
                        msg = 'Schedule "{}" (id={}) is {}.'.format(schedule["name"], schedule_id, schedule["status"])
                        if schedule["status"] != status:
                            msg += " Changing to {}.".format(status)
                            requests.put("{}/{}".format(url, schedule_id), data=json.dumps({'status': status}))
                            logging.warning(msg)
                        else:
                            logging.info(msg)
        except (ConnectionError, PermissionError):
            logging.critical("Unable to connect to hue bridge using {}".format(self._url_prefix))


class UnifiClient:
    """
    Connects to the Unifi controller, retrieves the wifi clients information, updates Hue schedules.
    """

    def __init__(self, args):
        for mandatory_value in ["unifi_host", "unifi_port", "unifi_username", "unifi_password"]:
            if mandatory_value not in args or vars(args)[mandatory_value] is None:
                raise ValueError("{} not specified in the config file nor on the command line.".format(mandatory_value))

        self._url_prefix = "https://{}:{}".format(args.unifi_host, args.unifi_port)
        self._auth_json = {"username": args.unifi_username, "password": args.unifi_password, "strict": True}
        self._unifi_session = requests.session()
        self._logged_in = False
        self._current_wifi_clients = []
        self._wifi_clients = args.wifi_clients
        self._someone_home = False
        self._interval = args.interval
        self.hc = HueClient(args)
        self._zmq = ZmqPublisher(args)

    @property
    def someone_home(self) -> bool:
        """
        True when a device to monitor is found connected to the unifi system.
        """
        return self._someone_home

    @someone_home.setter
    def someone_home(self, value: bool):
        self._someone_home = value
        self.hc.change_schedules(self._someone_home)

    @property
    def logged_in(self) -> bool:
        """
        Our connection status to unifi.
        """
        return self._logged_in

    @logged_in.setter
    def logged_in(self, value: bool):
        self._logged_in = value

    def _login(self) -> bool:
        auth_data = json.dumps(self._auth_json)
        logging.debug(auth_data)
        try:
            login_response = self._unifi_session.post(url="{}{}".format(self._url_prefix, __unifi_api_login__),
                                                      verify=False,
                                                      data=auth_data)
        except ConnectionError:
            logging.critical("Unable to connect to the Unifi controller using {}".format(self._url_prefix))
            return False
        self.logged_in = login_response.ok
        return self.logged_in

    def _get_clients_info(self) -> str:
        while not self.logged_in:
            self._login()
            time.sleep(self._interval)
        get_response = self._unifi_session.get(url="{}{}".format(self._url_prefix, __unifi_api_clients_stats__),
                                               verify=False)
        if get_response.status_code == 200:
            if isinstance(get_response.content, bytes):
                return get_response.content.decode()
            else:
                return get_response.content
        else:
            self.logged_in = False
            return ""

    def _parse_clients_info(self):
        self._current_wifi_clients = []
        clients = json.loads(self._get_clients_info())
        for client in clients["data"]:
            if not client["is_wired"]:
                wc = {}
                for prop in ["mac", "name", "hostname", "last_seen"]:
                    if prop in client:
                        wc[prop] = client[prop]
                wc["msg_ts"] = int(datetime.now().timestamp())
                self._current_wifi_clients.append(wc)
        if self._zmq.available:
            self._zmq.send_client_info(self._current_wifi_clients)

        logging.debug(self._current_wifi_clients)

    def _eval_is_someone_home(self):
        rtn = 0
        for c in self._current_wifi_clients:
            logging.debug(c.values())
            logging.debug(self._wifi_clients)
            set_wifi = set(self._wifi_clients).intersection(c.values())
            if len(set_wifi):
                logging.debug(set_wifi)
            rtn += len(set_wifi)
        self.someone_home = bool(rtn)

    def current_wifi_clients(self) -> list:
        """
        List of devices connected to Unifi. Each device is a dictionary with at least the mac address.
        """
        self._parse_clients_info()
        return self._current_wifi_clients

    def run(self):
        """
        Loops on getting client information from Unifi, updating the schedules accordingly.
        """
        while True:
            self.current_wifi_clients()
            self._eval_is_someone_home()
            time.sleep(self._interval)


class Huunifie:
    """
    Main class
    """

    def __init__(self):
        self.configuration = self._read_cli_arguments()
        pap = PaPLogger()
        self.config_file = Path(self.configuration.config_file)
        if self.config_file.exists():
            self.load_config()
        else:
            logging.warning("Configuration file {} not found.".format(str(self.config_file)))

        if self.configuration.save_config:
            self.save_config()

        pap.level = DEBUG if self.configuration.debug else INFO
        pap.verbose_fmt = self.configuration.verbose
        pap.log_file = self.configuration.log_file
        pap.syslog_port = self.configuration.syslog_port
        pap.syslog_host = self.configuration.syslog_host

        urllib3.disable_warnings()

    def save_config(self):
        """
        Save current settings to configuration file
        """

        h_config = configparser.ConfigParser()

        h_config["general"] = {}
        if not self.configuration.interval:
            self.configuration.interval = __interval__
        h_config["general"]["interval"] = str(self.configuration.interval)
        if not self.configuration.wifi_clients:
            self.configuration.wifi_clients = __wifi_clients_example__
        h_config["general"]["wifi_clients"] = ",".join(self.configuration.wifi_clients)
        if not self.configuration.schedules_names:
            self.configuration.schedules_names = __schedules_names_example__
        h_config["general"]["schedules_name"] = ",".join(self.configuration.schedules_names)

        h_config["unifi"] = {}
        if not self.configuration.unifi_host:
            self.configuration.unifi_host = __unifi_controller_host__
        h_config["unifi"]["host"] = self.configuration.unifi_host
        if not self.configuration.unifi_port:
            self.configuration.unifi_port = __unifi_controller_port__
        h_config["unifi"]["port"] = str(self.configuration.unifi_port)
        if not self.configuration.unifi_username:
            self.configuration.unifi_username = __unifi_controller_user__
        h_config["unifi"]["username"] = self.configuration.unifi_username
        if not self.configuration.unifi_password:
            self.configuration.unifi_password = __unifi_controller_pwd__
        h_config["unifi"]["password"] = self.configuration.unifi_password

        h_config["hue"] = {}
        if not self.configuration.hue_host:
            self.configuration.hue_host = __hue_hub_host__
        h_config["hue"]["host"] = self.configuration.hue_host
        if not self.configuration.hue_port:
            self.configuration.hue_port = __hue_hub_port__
        h_config["hue"]["port"] = str(self.configuration.hue_port)
        if not self.configuration.hue_key:
            self.configuration.hue_key = __hue_key__
        h_config["hue"]["key"] = self.configuration.hue_key

        h_config["zmq"] = {}
        if not self.configuration.pub_host:
            self.configuration.pub_host = __zmq_default_publishing_host__
        h_config["zmq"]["host"] = self.configuration.pub_host
        if not self.configuration.pub_port:
            self.configuration.pub_port = __zmq_default_publishing_port__
        h_config["zmq"]["port"] = str(self.configuration.pub_port)
        if "no_pub" in self.configuration:
            h_config["zmq"]["disabled"] = str(int(self.configuration.no_pub))

        h_config["logging"] = {}
        if self.configuration.syslog_host:
            h_config["logging"]["syslog_host"] = self.configuration.syslog_host
            if self.configuration.syslog_port:
                h_config["logging"]["syslog_port"] = str(self.configuration.syslog_port)
        if self.configuration.log_file:
            h_config["logging"]["log_file"] = str(self.configuration.log_file)

        with self.config_file.open(mode='w') as configfile:
            h_config.write(configfile)
        logging.info("Configuration saved to {}".format(str(self.config_file)))

    def load_config(self):
        """
        Load settings from configuration file, unless otherwise provided on the command line.
        """
        h_config = configparser.ConfigParser()
        with self.config_file.open() as configfile:
            h_config.read_file(configfile)
        if not ("general" in h_config.keys() and "unifi" in h_config.keys() and "hue" in h_config.keys()):
            logging.warning("Configuration file {} is invalid.".format(self.config_file))
            return
        if not self.configuration.interval:
            self.configuration.interval = int(h_config["general"]["interval"])
        if not self.configuration.wifi_clients:
            self.configuration.wifi_clients = h_config["general"]["wifi_clients"].split(",")
        if not self.configuration.schedules_names:
            self.configuration.schedules_names = h_config["general"]["schedules_name"].split(",")
        if not self.configuration.unifi_host:
            self.configuration.unifi_host = h_config["unifi"]["host"]
        if not self.configuration.unifi_port:
            self.configuration.unifi_port = int(h_config["unifi"]["port"])
        if not self.configuration.unifi_username:
            self.configuration.unifi_username = h_config["unifi"]["username"]
        if not self.configuration.unifi_password:
            self.configuration.unifi_password = h_config["unifi"]["password"]
        if not self.configuration.hue_host:
            self.configuration.hue_host = h_config["hue"]["host"]
        if not self.configuration.hue_port:
            self.configuration.hue_port = int(h_config["hue"]["port"])
        if not self.configuration.hue_key:
            self.configuration.hue_key = h_config["hue"]["key"]

        if "general" in h_config.keys():
            if not self.configuration.pub_host:
                self.configuration.pub_host = h_config["zmq"]["host"]
            if not self.configuration.pub_port:
                self.configuration.pub_port = int(h_config["zmq"]["port"])
            if "no_pub" not in self.configuration:
                self.configuration.no_pub = bool(int(h_config["zmq"]["disabled"]))

        if "logging" in h_config.keys():
            if "syslog_host" in h_config["logging"].keys() and not self.configuration.syslog_host:
                self.configuration.syslog_host = h_config["logging"]["syslog_host"]
            if "syslog_port" in h_config["logging"].keys():
                self.configuration.syslog_port = int(h_config["logging"]["syslog_port"])
            if "log_file" in h_config["logging"].keys() and not self.configuration.log_file:
                self.configuration.log_file = Path(h_config["logging"]["log_file"])

        logging.info("Configuration loaded from {}".format(str(self.config_file)))
        logging.debug(self.configuration)

    def main(self):
        """
        Entry point.
        """
        try:
            uc = UnifiClient(self.configuration)
            uc.run()
        except ValueError:
            logging.info("One or mandatory argument is missing.")

    @staticmethod
    def _read_cli_arguments():
        parser = argparse.ArgumentParser(description=__desc__,
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter, epilog=__desc__)

        parser.add_argument("-uh", "--unifi_host", help="Unifi controller hostname", type=str)
        parser.add_argument("-up", "--unifi_port", help="Unifi controller port", type=int)
        parser.add_argument("-uu", "--unifi_username", help="Unifi controller username", type=str)
        parser.add_argument("-uw", "--unifi_password", help="Unifi controller password", type=str)

        parser.add_argument("-hh", "--hue_host", help="Hue hub hostname", type=str)
        parser.add_argument("-hp", "--hue_port", help="Hue hub port", type=int)
        parser.add_argument("-hk", "--hue_key", help="Hue hub API key", type=str)
        pub_group = parser.add_mutually_exclusive_group()

        pub_group.add_argument("--no_pub", help="Disables zmq publication", action='store_true',
                               default=argparse.SUPPRESS)
        pub_group.add_argument("--pub", help="Enables zmq publication", action='store_false', dest="no_pub",
                               default=argparse.SUPPRESS)

        parser.add_argument("--pub_host", help="Host for zmq publication", default=__zmq_default_publishing_host__,
                            type=str)
        parser.add_argument("--pub_port", help="Port for zmq publication", default=__zmq_default_publishing_port__,
                            type=int)

        parser.add_argument("-wc", "--wifi_clients",
                            help="Wifi clients (hostname or mac) to monitor. Clients names are separated by spaces.",
                            nargs="+", type=str)

        parser.add_argument("-sn", "--schedules_names",
                            help="""Schedules to respectively enable/disable based on the wifi clients presence/absence.
                                Schedule names with space(s) to be double-quoted.
                                Schedule names are separated by spaces.""",
                            nargs="+", type=str)

        parser.add_argument("-i", "--interval", help="Polling interval", type=int, default=3)

        parser.add_argument("-c", "--config_file",
                            help="Path to configuration file. A template can be created by using the -s option below.",
                            default=__config_path__, type=Path)

        parser.add_argument("-s", "--save_config",
                            help="Safe configuration given on the command line to the configuration file.",
                            action="store_true")

        parser.add_argument("-v", "--verbose", help="Prints events information on the console.", action="store_true")
        parser.add_argument("-d", "--debug", help="Verbose mode.", action="store_true")

        parser.add_argument("-l", "--log_file", help="Path to log file.", type=Path)

        parser.add_argument("-sh", "--syslog_host", help="Syslog hostname.", type=str)
        parser.add_argument("-sp", "--syslog_port", help="Syslog port.", type=int, default=514)

        return parser.parse_args()


__all__ = ["Huunifie"]
