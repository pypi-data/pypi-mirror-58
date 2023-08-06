from .constants import COMMANDS


class ResponseParser(object):
    GET_ALARM = 'get alarm'
    GET_ALARMS = 'alarms'
    CHANGE_ALARM = 'c alarm'
    STOP_RADIO = 'st radio'
    START_RADIO = 's radio'

    def __init__(self):
        self.parse_fun = {COMMANDS.GET_ALARMS: self.__get_alarms, COMMANDS.GET_ALARM: self.__get_alarm,
                          COMMANDS.CHANGE_ALARM: self.__change_alarm, COMMANDS.START_RADIO: self.__start_radio,
                          COMMANDS.STOP_RADIO: self.__stop_radio}

    def parse_response(self, cmd, args, response):
        return self.parse_fun.get(cmd)(args, response)

    def __get_alarms(self, args, response):
        return response

    def __get_alarm(self, args, response):
        return response

    def __change_alarm(self, args, response):
        return self.__get_alarm(args, response)

    def __stop_radio(self, args, response):
        return self.__radio_string(args, response)

    def __start_radio(self, args, response):
        return self.__radio_string(args, response)

    @staticmethod
    def __radio_string(response, args):
        return response
