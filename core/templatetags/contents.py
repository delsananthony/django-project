from django import template

register = template.Library()


@register.inclusion_tag('core/partials/contents.html')
def contents():
    pass
