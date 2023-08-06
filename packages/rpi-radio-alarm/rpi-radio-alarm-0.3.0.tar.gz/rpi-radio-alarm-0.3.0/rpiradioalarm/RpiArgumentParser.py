import os

from rpiradioalarm import COMMANDS, ALARM_IDX


class RpiArgumentParser(object):
    parse_fun: dict

    def __init__(self):
        self.parse_fun = {
            'name': self.parse_string,
            'on': self.parse_boolean,
            'hour': self.parse_number,
            'min': self.parse_number,
            'days': self.parse_int_list
        }

    def parse_arguments(self, message: str):
        cmd_val = raw_args = None

        for cmd in COMMANDS:
            if message.startswith(cmd.value):
                raw_args = message.replace(cmd.value, '')
                cmd_val = cmd
                break

        if not cmd_val:
            raise NotImplementedError(f'Message: "{message}" \n could not be parsed')

        args_splitted = [s for s in raw_args.split(' ') if s.replace(' ', '') != '']
        args = dict()

        if len(args_splitted) > 1:
            for i in range(1, len(args_splitted) - 1, 2):
                args[args_splitted[i]] = self.parse_fun.get(args_splitted[i])(args_splitted[i + 1])
            args[ALARM_IDX] = args_splitted[0]
        elif len(args_splitted) > 0:
            args = args_splitted[0]
        else:
            args = args_splitted

        return cmd_val, args

    @staticmethod
    def is_command(message: str):
        return message.startswith(os.getenv('CMD_PREFIX'))

    @staticmethod
    def parse_boolean(value):
        return value == 'true' or value == 'True'

    @staticmethod
    def parse_int_list(value):
        return [int(k) for k in value.split(',')]

    @staticmethod
    def parse_number(value):
        return int(value)

    @staticmethod
    def parse_string(value):
        return value
