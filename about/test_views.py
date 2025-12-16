from django.urls import reverse
from django.test import TestCase
from .models import About
from .forms import CollaborateForm


class TestAboutViews(TestCase):
    def setUp(self):
        self.about_content = About(
            title="About",
            content="This is a test",
        )
        self.about_content.save()

    def test_render_about_with_collab_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About", response.content)
        self.assertIsInstance(
            response.context['collab_form'],
            CollaborateForm
        )

    def test_successful_collaboration_request_submission(self):
        """
        Test for a successful collab POST request
        """
        form_data = {
            'name': 'test',
            'email': 'mail@test.com',
            'message': 'This is a message',
        }
        response = self.client.post(
            reverse('about'),
            form_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', response.content
        )
