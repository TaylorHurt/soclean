
# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse  # new


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("So Clean Amarillo Texas"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("So Clean Amarillo Texas"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("So Clean Amarillo Texas"))
        self.assertContains(
            response, "<h1>Amarillo Texas Window Cleaning Services</h1>")
