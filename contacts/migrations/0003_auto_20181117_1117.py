# Generated by Django 2.0.8 on 2018-11-17 11:17

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AlterField(
            model_name='phonebook',
            name='city',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(re.compile("^[a-zA-Z '\\-]+$"), 'Enter a valid city', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='phonebook',
            name='zip',
            field=models.CharField(blank=True, max_length=6, validators=[django.core.validators.RegexValidator(re.compile('^\\d{6}$'), 'Enter a valid 6 digit zip code', 'invalid')], verbose_name='Zip Code'),
        ),
    ]