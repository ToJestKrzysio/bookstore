from django.views.generic import TemplateView


class LogoutRedirect(TemplateView):
    template_name = "accounts/logout.html"
