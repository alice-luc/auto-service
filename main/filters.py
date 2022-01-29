from django.template.defaultfilters import register
from django.utils.translation import ugettext


@register.filter(name='template_trans')
def template_trans(text):
    try:
        return ugettext(text)
    except Exception:
        return text
