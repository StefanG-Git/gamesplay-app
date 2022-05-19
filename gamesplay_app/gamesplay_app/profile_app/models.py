from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name='First Name',
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name='Last Name',
        null=True,
        blank=True,
    )

    picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
    )
