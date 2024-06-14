from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def contact_football_crazy(request):
    """
    Renders the contact form page.

    Displays an individual instance of :model:`contact.Contact`.

    **Context**
        ``ContactForm``
            An instance of :form:`contact.ContactForm`.

    **Template**
    :template:`contact/contact.html`
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Contact request received! We'll try to respond within 2 working days.")  # noqa

    contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
        'on_contact_page' : True,
    }

    return render(request, template, context)