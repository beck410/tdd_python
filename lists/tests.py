# resolve: fn used to resolve URLs
# resolve(URL).func maps the url to a view
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_hoe_page_returns_correct_html(self):
        request = HttpRequest()
        response =home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))  #3
        self.assertIn(b'<title>To-Do lists</title>', response.content)  #4
        self.assertTrue(response.content.endswith(b'</html>'))
