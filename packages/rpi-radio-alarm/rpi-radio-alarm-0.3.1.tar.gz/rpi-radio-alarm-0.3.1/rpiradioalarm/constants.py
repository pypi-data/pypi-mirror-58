from enum import Enum

ALARM_IDX: str = 'alarm_idx'


class COMMANDS(Enum):
    GET_ALARM = 'get alarm'
    GET_ALARMS = 'alarms'
    CHANGE_ALARM = 'c alarm'
    STOP_RADIO = 'st radio'
    START_RADIO = 's radio'
