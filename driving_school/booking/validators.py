from django.core import exceptions


def validate_string_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != "_":
            raise exceptions.ValidationError('Ensure the value contains only letters, numbers, and underscore')


def validate_min_age(value):
    if value < 17:
        raise exceptions.ValidationError('You have to be at least 17 years old.')
