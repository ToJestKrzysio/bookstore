from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from accounts.forms import CustomUserCreationForm


class LogoutRedirect(TemplateView):
    template_name = "registration/logout.html"


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"
