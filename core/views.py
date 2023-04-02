from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView, ListView

from core.forms import LogInForm
from core.mixins import DjangoLedgerSecurityMixIn


class DjangoLoginView(LoginView):
    form_class = LogInForm
    template_name = 'core/login.html'
    extra_context = {
        'page_title': _('Login')
    }

    def get_success_url(self):
        return reverse('home')


class DjangoLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def home(request):
    return render(request, 'core/index.html')


class DashboardView(DjangoLedgerSecurityMixIn, ListView):
    template_name = 'core/home.html'
    PAGE_TITLE = _('My Dashboard')
    context_object_name = 'entities'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
    }
