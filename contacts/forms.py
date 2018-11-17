from django.forms import ModelForm
from contacts.models import *

class PhonebookForm(ModelForm):
    class Meta:
        model = Phonebook
        fields=['first_name', 'last_name',
                'phone_number', 'email', 'address',
                'city', 'zip', 'notes']
