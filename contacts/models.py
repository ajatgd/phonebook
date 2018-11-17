from django.db import models
from django.contrib.auth.models import User
import re
from django.core import validators
from phonenumber_field.modelfields import PhoneNumberField

class Phonebook(models.Model):
    first_name = models.CharField(max_length=50, validators=[
            validators.RegexValidator(re.compile('^[a-zA-Z \'\-]+$'), ('Enter a valid first_name'), 'invalid')
        ])
    last_name = models.CharField(max_length=50, blank=True, validators=[
            validators.RegexValidator(re.compile('^[a-zA-Z \'\-]+$'), ('Enter a valid last_name'), 'invalid')
        ])
    phone_number = PhoneNumberField(blank=True, help_text=('Put their primary phone number here. '
                                                           'Put additional phone numbers in the Notes field.'))
    email = models.EmailField(blank=True, unique=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True, validators=[
            validators.RegexValidator(re.compile('^[a-zA-Z \'\-]+$'), ('Enter a valid city'), 'invalid')
        ])

    zip = models.CharField("Zip Code", max_length=6, blank=True,
                           validators=[validators.RegexValidator(re.compile('^\d{6}$'),
                                                                 ('Enter a valid 6 digit zip code'), 'invalid')
        ])
    notes = models.TextField("Notes and Comments", blank=True)
