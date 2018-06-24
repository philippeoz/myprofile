from django.shortcuts import render
from django.views.generic import FormView
from django.conf import settings

from django.contrib.auth.forms import UserCreationForm

from backend.core.models import Usuario


class MyProfileUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("email",)


class RegisterView(FormView):
    form_class = MyProfileUserCreationForm
    template_name = 'registration/register.html'
    success_url = settings.LOGIN_URL

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
