from django.test import TestCase

class booktest(TestCase):
    def test_name_url(self):
        res = self.client.get('/books/')
        self.assertEqual(res.status_code, 200)
