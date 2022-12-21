from enum import Enum


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class WeekSchedule(ChoicesEnumMixin, Enum):
    monday = 'Monday'
    tuesday = 'Tuesday'
    wednesday = 'Wednesday'
    thursday = 'Thursday'
    friday = 'Friday'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class HourSchedule(ChoicesEnumMixin, Enum):
    nine = '9 AM'
    ten = '10 AM'
    eleven = '11 AM'
    twelve = '12 PM'
    thirteen = '13 PM'
    fourteen = '14 PM'
    fifteen = '15 PM'
    sixteen = '16 PM'
    seventeen = '17 PM'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]



