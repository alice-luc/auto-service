from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


@admin.register(Car)
class CarAdmin(TranslationAdmin):
    list_display = ('id', 'brand', 'model', 'year', 'price', 'mileage')
    list_display_links = ('id',)
    search_fields = ('brand', 'model', 'year', 'body', 'engine_volume', 'condition')
    list_filter = ('brand', 'model', 'year', 'body', 'engine_volume', 'condition')


@admin.register(Wheel)
class WheelAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id',)


@admin.register(WheelDrive)
class WheelDriveAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id',)


@admin.register(Condition)
class ConditionAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id',)


@admin.register(Engine)
class EngineAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id',)


@admin.register(Body)
class BodyAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id',)


@admin.register(Gearbox)
class GearboxAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id',)


@admin.register(CarPhoto)
class CarPhotoAdmin(TranslationAdmin):
    list_display = ('id', 'capture')
    list_display_links = ('id',)
    list_filter = ('capture', 'subject')
    search_fields = ('capture', 'subject')
