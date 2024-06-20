from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Register About using Summernote rich text editor
    """
    summernote_fields = ('content',)
