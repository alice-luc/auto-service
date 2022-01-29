from django import template

from ..models import ServiceType

register = template.Library()

@register.simple_tag()
def get_service_type():
    return ServiceType.objects.all()

