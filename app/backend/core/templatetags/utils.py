from django import template


register = template.Library()


@register.filter
def attr(field, attrs):
    attrs = attrs.split('|')
    attrs_dict = {}
    for attr in attrs:
        attr = attr.split('=')
        attrs_dict[attr[0]] = attr[1]
    return field.as_widget(
        attrs=attrs_dict
    )