from enum import Enum


class DataSourceLabel(Enum):
    PREDICTION = 'predict'
    TEST = 'test'
    TRAIN = 'train'


class Status(Enum):
    COMPLETED = 'Completed'
    ERROR = 'Error'
    IN_PROGRESS = 'In Progress'
    WAITING = 'Waiting'
