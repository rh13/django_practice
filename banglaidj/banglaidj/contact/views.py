from django.shortcuts import render, redirect
from .models import contact
from .forms import contactForm

# Create your views here.

def my_contact(request):
	contacts=contact.objects.all()
	con={'contacts': contacts }

	return render(request, 'contact/contact.html', con)


def add_contact(request):
	if request.method == 'POST':
		form = contactForm(request.POST)
		form.save()
		return redirect('contact-list')
	else:
		form = contactForm
		return render(request, 'contact/add_contact.html', {'form' : form})


def edit_contact(request, contact_id):
    contacts = contact.objects.get(id=contact_id)
    if request.method == 'POST':
        form = contactForm(request.POST, instance=contacts)
        form.save()
        return redirect('contact-list')
    else:
        form = contactForm(instance=contacts)
    return render(request, 'contact/edit_contact.html', { 'form' : form})


def delete_contact(request, contact_id):
	contacts = contact.objects.get(id=contact_id)
	contacts.delete()
	return redirect('contact-list')
