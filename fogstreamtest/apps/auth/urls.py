from django.conf.urls import url

from .views import (
    LoginView, RegisterView
)


urlpatterns = [
    url(r'^login', LoginView.as_view()),
    url(r'^register', RegisterView.as_view())
]
