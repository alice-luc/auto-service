from django.contrib import admin

from booking.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'date', 'time_start', 'time_finish', 'is_confirmed', 'is_paid')
    list_display_links = ('id',)
    list_filter = ('date', 'time_start', 'time_finish', 'is_confirmed', 'is_paid')
    search_fields = ('date', 'time_start', 'time_finish')
