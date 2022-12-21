from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from driving_school.accounts.validators import validate_string_alphanumeric, validate_min_age


class User(AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 32

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 32

    email = models.EmailField(unique=True,)

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_string_alphanumeric,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_string_alphanumeric,
        )
    )



