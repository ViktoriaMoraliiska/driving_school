from django.db import models


class CategoryPrice(models.Model):
    MAX_LEN_NAME = 30

    category_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
        unique=True,
    )

    price = models.FloatField(
        null=False,
        blank=False
    )

    description_practice = models.TextField(
        null=True,
        blank=True
    )

    description_theory = models.TextField(
        null=True,
        blank=True
    )

    description_test = models.TextField(
        null=True,
        blank=True
    )

    description_not_included = models.TextField(
        null=True,
        blank=True
    )







