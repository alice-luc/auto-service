from django.db import models
from django.urls import reverse


class Car(models.Model):

    brand = models.CharField(max_length=100, verbose_name='Brand')
    model = models.CharField(max_length=100, verbose_name='Model')
    year = models.PositiveIntegerField(verbose_name='Year')
    vin = models.CharField(max_length=50, verbose_name='VIN-number')
    engine_type = models.ForeignKey('Engine', verbose_name='Engine Type', on_delete=models.CASCADE)
    color = models.CharField(max_length=50, verbose_name='Color')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Price')
    gearbox = models.ForeignKey('Gearbox', verbose_name='Gearbox', on_delete=models.CASCADE)
    body = models.ForeignKey('Body', verbose_name='Body Type', on_delete=models.CASCADE)
    engine_volume = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Engine Volume')
    wheel_drive = models.ForeignKey('WheelDrive', verbose_name='Wheel Drive', on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField(verbose_name='Mileage')
    wheel = models.ForeignKey('Wheel', verbose_name='Wheel', on_delete=models.CASCADE)
    condition = models.ForeignKey('Condition', verbose_name='Condition', on_delete=models.CASCADE)
    warranty = models.BooleanField(verbose_name='Warranty')
    slug = models.SlugField(unique=True, verbose_name='URL Path', help_text="unique url path")

    def __str__(self):
        return f'{self.brand} {self.model} {self.engine_volume}СС {self.year}'

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class CarPhoto(models.Model):

    subject = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Car')
    capture = models.CharField(max_length=511, verbose_name='Capture', null=True)
    image = models.ImageField(verbose_name='Image', upload_to='cars/')

    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_id': self.pk})

    class Meta:
        verbose_name = 'Car Picture'
        verbose_name_plural = 'Car Pictures'


class WheelDrive(models.Model):
    title = models.CharField(max_length=50, verbose_name='Wheel Drive')
    slug = models.SlugField(unique=True, verbose_name='URL Postfix', null=True, help_text="unique url path")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Wheel Drive'
        verbose_name_plural = 'Wheels Drive'


class Wheel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Wheel')
    slug = models.SlugField(unique=True, verbose_name='URL Postfix', null=True, help_text="unique url path")

    def __str__(self):
        return self.title


class Condition(models.Model):
    title = models.CharField(max_length=50, verbose_name='Condition')
    slug = models.SlugField(unique=True, verbose_name='URL Postfix', null=True, help_text="unique url path")

    def __str__(self):
        return self.title


class Engine(models.Model):
    title = models.CharField(max_length=50, verbose_name='Engine')
    slug = models.SlugField(unique=True, verbose_name='URL Postfix', null=True, help_text="unique url path")

    def __str__(self):
        return self.title


class Body(models.Model):
    title = models.CharField(max_length=50, verbose_name='Body Type')
    slug = models.SlugField(unique=True, verbose_name='URL Postfix', null=True, help_text="unique url path")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Body Type'
        verbose_name_plural = 'Body Types'


class Gearbox(models.Model):
    title = models.CharField(max_length=50, verbose_name='Gearbox')
    slug = models.SlugField(unique=True, verbose_name='URL Postfix', null=True, help_text="unique url path")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gearbox'
        verbose_name_plural = 'Gearboxes'
