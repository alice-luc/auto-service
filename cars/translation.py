from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('color', 'description')


@register(Engine)
class EngineTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(WheelDrive)
class WheelDriveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Wheel)
class WheelTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Body)
class BodyTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Condition)
class ConditionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Gearbox)
class GearboxTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CarPhoto)
class CarPhotoTranslationOptions(TranslationOptions):
    fields = ('capture',)

