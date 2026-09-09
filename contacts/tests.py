from django.test import TestCase

from .forms import ContactForm
from .models import Contact


class ContactTests(TestCase):
	def test_email_validation_rejects_invalid_address(self):
		form = ContactForm(data={
			'name': 'Ana Perez',
			'phone': '+56 9 1234 5678',
			'email': 'correo-invalido',
			'address': 'Calle 123',
		})

		self.assertFalse(form.is_valid())
		self.assertIn('email', form.errors)

	def test_contact_can_be_created_and_found_by_name_or_email(self):
		Contact.objects.create(
			name='Ana Perez',
			phone='+56 9 1234 5678',
			email='ana@correo.cl',
			address='Calle 123',
		)

		name_response = self.client.get('/?q=Ana')
		email_response = self.client.get('/?q=correo.cl')

		self.assertContains(name_response, 'Ana Perez')
		self.assertContains(email_response, 'ana@correo.cl')
