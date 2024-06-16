from django.db import models


class NewsletterSubscription(models.Model):
    """
    Model representing a user's subscription to the newsletter.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        """
        String for representing the NewsletterSubscription object (email).
        """
        return self.email

    def unsubscribe(self):
        """
        Marks the subscriber as unsubscribed.
        """
        self.is_subscribed = False
        self.save()
        