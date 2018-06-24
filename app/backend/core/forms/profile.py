from django import forms

from backend.core.models import Usuario


class UsuarioProfileForm(forms.ModelForm):
    """
    Definição do Form para o 'profile' do Usuário
    """

    class Meta:
        model = Usuario
        fields = '__all__'


class UsuarioProfileSetupForm(forms.ModelForm):
    """
    Definição do Form parao 'setup' o 'profile' do Usuário
    """

    class Meta:
        model = Usuario
        fields = ('dados_publicos_api', )