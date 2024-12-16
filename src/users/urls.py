from django.urls import re_path
from .views import RegistrationView, LoginView

urlpatterns = [
    re_path(r'^auth/register/$', RegistrationView.as_view(), name='register'),
    re_path(r'^auth/login/$', LoginView.as_view(), name='login'),
]