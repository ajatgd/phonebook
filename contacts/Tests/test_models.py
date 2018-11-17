from django.test import TestCase
from ..models import Phonebook


class PhonebookTest(TestCase):

    def setUp(self):
        Phonebook.objects.create(
            first_name='Casper',
            last_name="dsouza",
            email='casper1@gmail.com',
            address='any address',
            city='any city',
            zip=256987,
            notes="any notes")
        Phonebook.objects.create(
            first_name='Raadu',
            last_name="dsouza1",
            email='casper21@yahoo.com',
            address='any address',
            city='any city',
            zip=256987,
            notes="any notes")

    def test_phonebook_contact(self):
        phonebook_casper = Phonebook.objects.get(first_name='Casper')
        phonebook_raadu = Phonebook.objects.get(first_name='Raadu')
        self.assertEqual(
            phonebook_casper.get_name(), "Casper dsouza")
        self.assertEqual(
            phonebook_raadu.get_name(), "Raadu dsouza1")
