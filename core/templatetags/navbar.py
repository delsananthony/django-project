from django import template

register = template.Library()


@register.inclusion_tag('core/partials/nav.html')
def navbar():
    pass
