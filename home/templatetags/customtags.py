from django import template

register = template.Library()

@register.simple_tag
def is_empty(queryset, category):
    return True if (queryset.filter(category=category).count()) else False
    