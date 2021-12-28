from django.test import TestCase
from ContactList.utils.rounting import APP_INITIAL, get_app_urls


class TestRouting(TestCase):
    def test_get_correct_app_urls(self):
        self.assertEqual(get_app_urls('authentication'),
                         f"{APP_INITIAL}.{'authentication'}.urls")
