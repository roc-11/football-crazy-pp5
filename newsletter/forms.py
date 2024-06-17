from crispy_forms.helper import FormHelper

from django import forms
from .models import NewsletterSubscription


class SubscriberForm(forms.ModelForm):
    """
    A form for handling email newsletter subscription requests.
    
    It extends Django's ModelForm and customizes its appearance 
    using crispy_formsand additional field modifications.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with additional settings.
        This method sets up a FormHelper to customize the form's appearance,
        modifies the 'email' field label, and adds a placeholder to the
        'email' field.
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].label = False
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'

    class Meta:
        model = NewsletterSubscription
        fields = ('email', 'is_subscribed')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.is_subscribed = True
        if commit:
            instance.save()
        return instance


class UnsubscribeForm(forms.Form):
    """
    A form for handling email unsubscribe requests.
    """
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'placeholder': 'Email address'})
    )


class NewsletterForm(forms.Form):
    subject = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
