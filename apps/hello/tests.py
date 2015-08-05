from django.test import TestCase, Client


class SomeTests(TestCase):
    def test_math(self):
        """ put docstrings in your tests """
        assert(2 + 2 == 4)


class ContactsTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_contacts(self):
        """ checking of contacts view """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

