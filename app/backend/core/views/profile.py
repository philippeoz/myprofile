from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db import transaction
from django.shortcuts import redirect

from backend.core.models import Usuario
from backend.core.forms import UsuarioProfileForm
from backend.core.forms import UsuarioProfileSetupForm
from backend.core.forms import UsuarioLivroFavoritoFormSet


def check_first_login(request):
    """
    Redireciona o usuário para Edição do Profile
    em caso de primeiro login
    """
    if request.user.is_anonymous:
        return redirect('login')
    first_login = request.session.get('first_login', None)
    return redirect(
        'profile-edit' if first_login else 'profile-public',
        pk=request.user.id
    )


class BaseUsuarioView:
    model = Usuario


class MyProfilePublicView(BaseUsuarioView, DetailView):
    pass


class MyProfileEditView(BaseUsuarioView, LoginRequiredMixin, UpdateView):
    form_class = UsuarioProfileForm

    def get_initial(self):
        initial = super(MyProfileEditView, self).get_initial()
        self.object = self.get_object()
        return initial

    def get_context_data(self, **kwargs):
        if 'filmes_favoritos_formset' not in kwargs:
            filmes_favoritos = UsuarioLivroFavoritoFormSet(prefix='filmes_favoritos')
            f_count = self.object.filmes_favoritos.count()
            filmes_favoritos.extra = f_count if f_count else 1
            for index, filme_favorito in enumerate(self.object.filmes_favoritos.all()):
                filmes_favoritos.forms[index].initial = filme_favorito.__dict__
                filmes_favoritos.forms[index].initial['usuario'] = self.request.user.id
            for filme_favorito in filmes_favoritos.extra_forms:
                filme_favorito.initial['usuario'] = self.request.user.id
            kwargs['filmes_favoritos_formset'] = filmes_favoritos
        return super(MyProfileEditView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        filmes_favoritos_formset = UsuarioLivroFavoritoFormSet(
            self.request.POST, prefix='filmes_favoritos')
        if form.is_valid() and filmes_favoritos_formset.is_valid():
            return self.form_valid(form, filmes_favoritos_formset)
        else:
            import pdb; pdb.set_trace()
            return self.form_invalid(form, filmes_favoritos_formset)

    def form_valid(self, form, filmes_favoritos_formset):       
        with transaction.atomic():
            self.object = form.save()
            self.formset_validation(filmes_favoritos_formset)
        return super(MyProfileEditView, self).form_valid(form)
    
    def form_invalid(self, form, filmes_favoritos_formset):
        return super(MyProfileEditView, self).form_invalid(form)
    
    def formset_validation(self, formset):
        for form in formset:
            model_object = form.update_create_delete_in_formset()
            if model_object is not None:
                model_object.usuario = self.object
                model_object.save()


class MyProfileSetupView(BaseUsuarioView, LoginRequiredMixin, UpdateView):
    form_class = UsuarioProfileSetupForm
