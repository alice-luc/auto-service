from django.db import models
from django.urls import reverse


class ServiceType(models.Model):
    title = models.CharField(max_length=150, verbose_name='Service Name', default='Maintenance')
    slug = models.SlugField(unique=True, verbose_name='URL Postfix', help_text="unique url path")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services', kwargs={'service_type_slug': self.slug})

    class Meta:
        verbose_name = 'Service Type'
        verbose_name_plural = 'Service Types'


class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name='Service Name')
    description = models.TextField(verbose_name='Description')
    duration = models.PositiveIntegerField(verbose_name='Duration')
    photo = models.ImageField(verbose_name='Service Picture', null=True, blank=True, upload_to='services/')
    prefix = models.CharField(max_length=50, verbose_name='Price prefix', default='starts with', blank=True)
    postfix = models.CharField(max_length=50, verbose_name='Time Rate', default='/h', blank=True)
    default_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price')
    service_type = models.ForeignKey(ServiceType, verbose_name='Service Type', on_delete=models.CASCADE,
                                     related_name='service_type')
    slug = models.SlugField(unique=True, verbose_name='URL Postfix', help_text="unique url path")
    related_service = models.ForeignKey('self', blank=True, null=True, verbose_name='Related Service',
                                        related_name='rel_one', on_delete=models.SET_NULL)
    related_service_two = models.ForeignKey('self', blank=True, null=True, verbose_name='Related Service 2',
                                            related_name='rel_two', on_delete=models.SET_NULL)
    price_depends = models.BooleanField(verbose_name='Price depends?', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Price(models.Model):
    price_from = models.PositiveIntegerField(verbose_name='Price From')
    price_to = models.PositiveIntegerField(verbose_name='Price To')
    body = models.ForeignKey('cars.Body', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service')

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'
