from django.contrib import admin
from .models import NewsletterSubscription


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    """
    This class defines the custom configuration for displaying and ordering
    NewsletterSubscription records in the Django admin site.
    """
    list_display = ('email', 'is_subscribed', 'subscribed_at')

    ordering = ('-subscribed_at',)


admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)
