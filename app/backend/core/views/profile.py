from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.shortcuts import redirect

from backend.core.models import Usuario


class BaseUsuarioView:
    model = Usuario

class MyProfilePublicView(BaseUsuarioView, DetailView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.last_login is None:
            return redirect('profile-edit')
        return super(MyProfilePublicView, self).dispatch(request, *args, **kwargs)


class MyProfileEditView(BaseUsuarioView, UpdateView):
    pass


class MyProfileSetupView(BaseUsuarioView, UpdateView):
    pass
