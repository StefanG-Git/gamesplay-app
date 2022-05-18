from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Game(models.Model):
    TITLE_MAX_LENGTH = 30
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0
    MAX_LEVEL_MIN_VALUE = 1

    CATEGORY_MAX_LENGTH = 15
    CATEGORIES = (
        'Action',
        'Adventure',
        'Puzzle',
        'Strategy',
        'Sports',
        'Board/Card Game',
        'Other',
    )

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        choices=[(c, c) for c in CATEGORIES],
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE),
        ),
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(MAX_LEVEL_MIN_VALUE),
        ),
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('title',)
