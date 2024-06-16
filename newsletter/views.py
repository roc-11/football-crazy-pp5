from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect

from .models import NewsletterSubscription
from .forms import SubscriberForm, UnsubscribeForm, NewsletterForm


def add_subscriber(request):
    """
    Add email to the subscriber list.
    This view function handles the
    addition of an email address to the subscriber list.
    It uses the SubscriberForm to
    validate and save the email address.
    If the email already exists in the database,
    an error message is displayed.
    Otherwise, the email is saved, and a success message is shown.
    """
    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        if NewsletterSubscription.objects.filter(email=instance.email).exists():
            messages.error(request,
                f"{instance.email} already exists in our database. "
                "Please check your email and try again."
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        instance.save()
        messages.info(request,
            f"{instance.email} has been added to our the newsletter"
        )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unsubscribe(request):
    """
    This view handles the unsubscription
    process based on a submitted form.
    If the request method is POST,
    it validates the UnsubscribeForm, attempts to
    find a subscriber with the provided email address,
    and marks them as unsubscribed.
    Success and error messages are displayed accordingly.
    If the form is not valid, an error message is
    shown for invalid form submission.
    """
    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                subscriber = NewsletterSubscription.objects.get(email=email)
                subscriber.unsubscribe()
                messages.info(request,
                    f"Successfully unsubscribed {email} from our newsletter."
                )
            except Subscriber.DoesNotExist:
                messages.error(request,
                    f"No subscriber found with the email {email}. "
                    f"Please check your email and try again."
                )
        else:
            messages.error(request,
                "Invalid form submission. Check your input and try again."
            )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def send_newsletter(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can access this page.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            subscribers = NewsletterSubscription.objects.all().values_list('email', flat=True)
            html_content = render_to_string('newsletter/newsletter_template.html', {'subject': subject, 'content': content})
            send_mail(subject, content, settings.EMAIL_HOST_USER, subscribers, fail_silently=False)
            messages.success(request, 'Newsletter Sent Succesfully')
            return redirect('profile')
        else:
            messages.error(request, 'Failed to send newsletter')
    else:
        form = NewsletterForm()

    context = {
        'form': form, 
        'from_profile' : True,
    }
    return render(request, 'newsletter/send_email.html', context)
