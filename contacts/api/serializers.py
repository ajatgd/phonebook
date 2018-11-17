from rest_framework import serializers
from contacts import models

class PhonebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phonebook
        fields = ('id','first_name', 'last_name',
                  'phone_number', 'email', 'address',
                  'city', 'zip', 'notes')
