from django.test import TestCase

class acctest(TestCase):
    def test_name_url(self):
        res = self.client.get('/accounts/login/')
        self.assertEqual(res.status_code, 200)