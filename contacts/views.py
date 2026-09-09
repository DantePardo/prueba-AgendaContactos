from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Contact


def contact_list(request):
	# q permite filtrar sin distinguir mayúsculas y minúsculas.
	query = request.GET.get('q', '').strip()
	contacts = Contact.objects.all()
	if query:
		contacts = contacts.filter(Q(name__icontains=query) | Q(email__icontains=query))

	# El formulario se procesa solo al recibir una solicitud POST válida.
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('contact_list')
	else:
		form = ContactForm()

	return render(request, 'contacts/contact_list.html', {
		'contacts': contacts,
		'form': form,
		'query': query,
	})
