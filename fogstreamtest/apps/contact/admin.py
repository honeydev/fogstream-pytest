from django.contrib import admin
from . models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'mail_send', 'author')
