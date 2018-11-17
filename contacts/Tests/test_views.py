
from django.shortcuts import reverse
from rest_framework.test import APITestCase
import json
from ..models import Phonebook
from rest_framework import status

from django.test import TestCase, Client
from django.urls import reverse
from contacts.api.serializers import PhonebookSerializer

client = Client()


class GetAllPhonebookTest(TestCase):
    """ Test module for GET all phonebook API """

    def setUp(self):
        self.phonebook1=Phonebook.objects.create(
            first_name='Casper',
            last_name="dsouza",
            email='casper1@gmail.com',
            address='any address',
            city='any city',
            zip=256987,
            notes="any notes")
        self.phonebook2=Phonebook.objects.create(
            first_name='rohan',
            last_name="mishra",
            email='rohan@gmail.com',
            address='any address',
            city='any city',
            zip=256987,
            notes="any notes")

    def test_get_valid_single_phonebook(self):
        response = client.get(
            reverse('detail', kwargs={'pk': self.phonebook1.pk}))
        phonebook = Phonebook.objects.get(pk=self.phonebook1.pk)
        serializer = PhonebookSerializer(phonebook)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




class CreateNewPhonebookTest(TestCase):
    """ Test module for inserting a new phonebook """

    def setUp(self):
        self.valid_payload = {
            "first_name":'rohan',
            "last_name":"mishra",
            "email":'roha1@gmail.com',
            "address":'any address',
            "city":'any city',
            "zip":256987,
            "notes":"any notes"
        }
        self.invalid_payload = {
            "first_name":'',
            "last_name":"mishra",
            "email":'roha1@gmail.com',
            "address":'any address',
            "city":'any city',
            "zip":256987,
            "notes":"any notes"
        }

    def test_create_valid_phonebook(self):
        response = client.post(
            reverse('create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_invalid_phonebook(self):
        response = client.post(
            reverse('create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePhonebookTest(TestCase):
    """ Test module for updating an existing phonebook record """

    def setUp(self):
        self.phonebook1=Phonebook.objects.create(
            first_name='Casper',
            last_name="dsouza",
            email='casper1@gmail.com',
            address='any address',
            city='any city',
            zip=256987,
            notes="any notes")
        self.phonebook2=Phonebook.objects.create(
            first_name='rohan',
            last_name="mishra",
            email='rohan@gmail.com',
            address='any address',
            city='any city',
            zip=256987,
            notes="any notes")
        self.valid_payload = {
            "first_name":'rohan',
            "last_name":"mishra",
            "email":'roha1@gmail.com',
            "address":'any address',
            "city":'any city',
            "zip":256987,
            "notes":"any notes"
        }
        self.invalid_payload = {
            "first_name":'',
            "last_name":"mishra",
            "email":'roha1@gmail.com',
            "address":'any address',
            "city":'any city',
            "zip":256987,
            "notes":"any notes"
        }

    def test_valid_update_phonebook(self):
        response = client.put(
            reverse('update', kwargs={'pk': self.phonebook1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_phonebook(self):
        response = client.put(
            reverse('update', kwargs={'pk': self.phonebook2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSinglePhonebookTest(TestCase):
    """ Test module for deleting an existing phonebook record """

    def setUp(self):
        self.phonebook1=Phonebook.objects.create(
            first_name='Casper',
            last_name="dsouza",
            email='casper1@gmail.com',
            address='any address',
            city='any city',
            zip=256987,
            notes="any notes")
        self.phonebook2=Phonebook.objects.create(
            first_name='rohan',
            last_name="mishra",
            email='rohan@gmail.com',
            address='any address',
            city='any city',
            zip=256987,
            notes="any notes")

    def test_valid_delete_phonebook(self):
        response = client.delete(
            reverse('delete', kwargs={'pk': self.phonebook1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_phonebook(self):
        response = client.delete(
            reverse('delete', kwargs={'pk': 300}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
