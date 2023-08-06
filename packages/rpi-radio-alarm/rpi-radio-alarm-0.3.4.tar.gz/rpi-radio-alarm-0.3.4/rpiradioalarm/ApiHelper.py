import json
import os
from http.client import HTTPConnection
from dotenv import load_dotenv
from .constants import COMMANDS, ALARM_IDX
from .RpiResponseParser import ResponseParser


class ApiHelper(object):
    conn: HTTPConnection
    response_parser: ResponseParser

    def __init__(self, response_parser=ResponseParser()):
        load_dotenv()
        self.response_parser = response_parser
        self.FUNCTIONS = {COMMANDS.GET_ALARMS: self.__get_alarms, COMMANDS.GET_ALARM: self.__get_alarms,
                          COMMANDS.CHANGE_ALARM: self.__change_alarm, COMMANDS.START_RADIO: self.__start_radio,
                          COMMANDS.STOP_RADIO: self.__stop_radio}

    def do_command(self, cmd, args):
        self.conn = HTTPConnection(os.getenv('RPI-RADIO-ALARM-URL'))
        return self.response_parser.parse_response(cmd, args, self.FUNCTIONS.get(cmd)(args))

    def __get_alarms(self, args):
        has_args = len(args) > 0
        if has_args:
            self.conn.request("GET", '/alarm/' + str(args).replace(' ', ''))
        else:
            self.conn.request("GET", "/alarm")
        resp = json.loads(self.conn.getresponse().read().decode())

        if isinstance(resp, dict):
            resp = [resp]
        return resp

    def __change_alarm(self, args=dict):
        alarm_id = args.pop(ALARM_IDX)
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        self.conn.request("PUT", "/alarm/" + str(alarm_id), json.dumps(args), headers=headers)
        resp = json.loads(self.conn.getresponse().read().decode())
        return resp

    def __start_radio(self, args):
        return self.__change_radio(True)

    def __stop_radio(self, args):
        return self.__change_radio(False)

    def __change_radio(self, running: bool):
        headers = {"Content-type": "application/json"}
        self.conn.request("POST", "/radio", json.dumps({"switch": "on" if running else "off"}), headers=headers)
        resp = json.loads(self.conn.getresponse().read().decode())
        return resp
