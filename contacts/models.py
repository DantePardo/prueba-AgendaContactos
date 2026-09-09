from django.db import models


class Contact(models.Model):
	# El modelo representa los datos básicos de una persona en la agenda.
	name = models.CharField('nombre', max_length=120)
	phone = models.CharField('teléfono', max_length=30)
	email = models.EmailField('correo electrónico')
	address = models.CharField('dirección', max_length=200)
	created_at = models.DateTimeField('fecha de creación', auto_now_add=True)

	class Meta:
		ordering = ['name']
		verbose_name = 'contacto'
		verbose_name_plural = 'contactos'

	def __str__(self):
		return self.name
