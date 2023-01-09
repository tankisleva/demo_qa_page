import dataclasses
import datetime
from enum import Enum

import framework


# class Gender(Enum):
#     Male = 1
#     Female = 2
#     Other = 3
#
#
# class Hobby(Enum):
#     Music = 'Music'
#     Reading = 'Reading'
#     Sports = 'Sports'
#
#
# def format_input_date(value: datetime.date):
#     return value.strftime(framework.config.datetime_input_format)
#
#
# def format_view_date(value: datetime.date):
#     return value.strftime(framework.config.datetime_view_format)


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    birthday_year: str
    birthday_month: str
    birthday_day: int
    subject: str
    hobby: str
    image: str
    address: str
    state: str
    city: str
