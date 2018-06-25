from django import forms
from django.forms import formset_factory

from backend.core.models import Usuario
from backend.core.models import UsuarioFilmeFavorito


class UsuarioProfileForm(forms.ModelForm):
    """
    Definição do Form para o 'profile' do Usuário
    """

    class Meta:
        model = Usuario
        fields = [
            'foto',
            'first_name',
            'last_name',
            'data_nascimento',
            'sexo',
            'pais',
            'estado',
            'cidade'
        ]


class UsuarioProfileSetupForm(forms.ModelForm):
    """
    Definição do Form para o 'setup' o 'profile' do Usuário
    """
    class Meta:
        model = Usuario
        fields = ('dados_publicos_api', )


class UsuarioFilmeFavoritoForm(forms.ModelForm):
    """
    Definição de Form para Filmes Favoritos dos Usuários
    """
    class Meta:
        model = UsuarioFilmeFavorito
        fields = ('titulo', )
    
    def update_create_delete_in_formset(self):
        delete = self.cleaned_data.get('DELETE', None)
        model_id = self.cleaned_data.get('id', None)

        if model_id is not None:
            model_object = self._meta.model.objects.get(id=model_id)
        else:
            model_object = None

        if model_object is not None:
            if delete is True:
                model_object.delete()
                model_object = None
            else:
                for key, value in self.cleaned_data.items():
                    if key != 'id' and hasattr(model_object, key):
                        setattr(model_object, key, value)
        elif delete is False:
            model_object = self.save(commit=False)
        return model_object


UsuarioLivroFavoritoFormSet = formset_factory(
    form=UsuarioFilmeFavoritoForm,
    extra=0,
    can_delete=True
)