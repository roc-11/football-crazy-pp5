from .forms import SubscriberForm


def render_subscribe_form(request):
    """
    Render subscribe form across all pages.
    This function creates an instance of the SubscriberForm to be used
    for rendering a subscribe form consistently across different pages.
    """

    subscribe_form = SubscriberForm()

    context = {
        'subscribe_form': subscribe_form,
    }

    return context