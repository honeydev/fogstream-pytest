from django.conf.urls import url

from .views import (
    CreateContactMessage
)


urlpatterns = [
    url(r'^contact-message/create', CreateContactMessage.as_view()),
]
