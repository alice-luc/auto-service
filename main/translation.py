from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'prefix', 'postfix')


@register(ServiceType)
class ServiceTypeTranslationOptions(TranslationOptions):
    fields = ('title', )
