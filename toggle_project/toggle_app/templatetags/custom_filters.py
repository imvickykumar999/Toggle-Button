from django import template

register = template.Library()

@register.filter
def length_is(value, length):
    """Check if the length of the value is equal to the given length."""
    try:
        return len(value) == int(length)
    except (ValueError, TypeError):
        return False
