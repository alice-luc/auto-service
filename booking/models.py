from django.db import models


class Booking(models.Model):

    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    description = models.TextField(blank=True, verbose_name='Description')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.PositiveBigIntegerField(verbose_name='Phone number')
    date = models.DateField(verbose_name='Date')
    time_start = models.TimeField(verbose_name='Starts at')
    time_finish = models.TimeField(verbose_name='Finishes at')
    service = models.ForeignKey('main.Service', verbose_name='Service', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created At')
    is_confirmed = models.BooleanField(default=True, verbose_name='Confirm?')
    is_paid = models.BooleanField(default=False, verbose_name='Paid?')

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

