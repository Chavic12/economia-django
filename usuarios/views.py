from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from .forms import FormularioLogin, RegistroForm


class loginUsuario(FormView):
    template_name = 'auth/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('ambiental')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("Ingreso en if de request")
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(loginUsuario,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(loginUsuario,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')


class RegistroUsuario(CreateView):
    model = User
    template_name = "auth/register.html"
    form_class = RegistroForm
    success_url = reverse_lazy('inicio')


