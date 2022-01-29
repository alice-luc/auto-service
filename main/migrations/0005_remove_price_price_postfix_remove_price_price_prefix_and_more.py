# Generated by Django 4.0.1 on 2022-01-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220127_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='price_postfix',
        ),
        migrations.RemoveField(
            model_name='price',
            name='price_prefix',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='postfix',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='postfix_en',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='postfix_fi',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='postfix_ru',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='prefix',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='prefix_en',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='prefix_fi',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='prefix_ru',
        ),
        migrations.AddField(
            model_name='service',
            name='postfix',
            field=models.CharField(blank=True, default='/h', max_length=50, verbose_name='Time Rate'),
        ),
        migrations.AddField(
            model_name='service',
            name='postfix_en',
            field=models.CharField(blank=True, default='/h', max_length=50, null=True, verbose_name='Time Rate'),
        ),
        migrations.AddField(
            model_name='service',
            name='postfix_fi',
            field=models.CharField(blank=True, default='/h', max_length=50, null=True, verbose_name='Time Rate'),
        ),
        migrations.AddField(
            model_name='service',
            name='postfix_ru',
            field=models.CharField(blank=True, default='/h', max_length=50, null=True, verbose_name='Time Rate'),
        ),
        migrations.AddField(
            model_name='service',
            name='prefix',
            field=models.CharField(blank=True, default='starts with', max_length=50, verbose_name='Price prefix'),
        ),
        migrations.AddField(
            model_name='service',
            name='prefix_en',
            field=models.CharField(blank=True, default='starts with', max_length=50, null=True, verbose_name='Price prefix'),
        ),
        migrations.AddField(
            model_name='service',
            name='prefix_fi',
            field=models.CharField(blank=True, default='starts with', max_length=50, null=True, verbose_name='Price prefix'),
        ),
        migrations.AddField(
            model_name='service',
            name='prefix_ru',
            field=models.CharField(blank=True, default='starts with', max_length=50, null=True, verbose_name='Price prefix'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
