from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import NewsletterSubscription
from .forms import SubscriberForm, UnsubscribeForm


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
