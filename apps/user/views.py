# -*- coding:utf-8 -*-

from django.views.generic import CreateView, RedirectView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
from core.mixins import GuestMixin
from django.shortcuts import redirect

class LogoutView(RedirectView):
    def logout_user(request):
        logout(request)
        return redirect("/")


class LoginView(GuestMixin, FormView):

    def login_user(request):
        logout(request)
        email = password = ''
        if request.POST:
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        return redirect("/")
