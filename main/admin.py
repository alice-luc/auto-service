from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description', 'default_price', 'service_type', 'prefix', 'postfix')
    list_display_links = ('id',)
    list_filter = ('service_type', 'default_price')
    search_fields = ('title', 'service_type')


@admin.register(ServiceType)
class ServiceTypeAdmin(TranslationAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'body', 'price_from', 'price_to')
    list_display_links = ('id',)
    list_filter = ('service', 'body')
    search_fields = ('service', 'body')
