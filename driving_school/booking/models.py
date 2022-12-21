from django.core import validators
from django.core.mail import send_mail
from django.db import models

from driving_school import settings
from driving_school.booking.mixins import WeekSchedule, HourSchedule
from driving_school.booking.validators import validate_string_alphanumeric


class BookingModel(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 32

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 32

    email = models.EmailField(
        null=False,
        blank=False,
        unique=False,
    )

    phone_number = models.IntegerField(
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_string_alphanumeric,
        )
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_string_alphanumeric,
        )
    )

    week_schedule = models.CharField(
        null=False,
        blank=False,
        choices=WeekSchedule.choices(),
        max_length=20
    )

    hour_schedule = models.CharField(
        null=False,
        blank=False,
        choices=HourSchedule.choices(),
        max_length=20,
    )

    text_message = models.TextField(
        null=True,
        blank=True,
    )


