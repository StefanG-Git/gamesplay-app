from django import template
from gamesplay_app.profile_app.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0
