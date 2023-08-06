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

    def parse_response(self, cmd, response, args):
        return self.parse_fun.get(cmd)(response, args)

    def __get_alarms(self, response, args):
        return response

    def __get_alarm(self, response, args):
        return response

    def __change_alarm(self, response, args):
        return self.__get_alarm(response, args)

    def __stop_radio(self, response, args):
        return self.__radio_string(response, args)

    def __start_radio(self, response, args):
        return self.__radio_string(response, args)

    @staticmethod
    def __radio_string(response, args):
        return response
