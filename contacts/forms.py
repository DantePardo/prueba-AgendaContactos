from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
	# ModelForm reutiliza las reglas del modelo, incluida la validación de EmailField.
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ej. Ana Perez'}),
            'phone': forms.TextInput(attrs={'placeholder': '+56 9 1234 5678'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ana@correo.cl'}),
            'address': forms.TextInput(attrs={'placeholder': 'Calle y numero'}),
        }
