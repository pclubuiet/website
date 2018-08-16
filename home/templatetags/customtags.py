from django import template

register = template.Library()

@register.simple_tag
def is_empty(queryset, category):
    print(queryset, category, "sdfdf", queryset.filter(category=category).count())
    return True if (queryset.filter(category=category).count()) else False

@register.filter(name='split')
def split(value, key):
    return value.split(key)
