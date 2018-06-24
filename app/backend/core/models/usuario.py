from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField

from backend.core.manager import UserManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    """Model para Usuários do sistema"""

    # foto, nome, idade, sexo, país, estado, cidade e filmes favoritos
    # Foto
    foto = ProcessedImageField(
        upload_to='fotos',
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True
    )
    foto_thumbnail = ImageSpecField(
        source='foto', format='JPEG', options={'quality': 60})
    data_nascimento = models.DateField(
        _('data de nascimento'),
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True
    )
    sexo = models.NullBooleanField()
    pais = models.CharField(_('país'), max_length=255, blank=True, null=True)
    estado = models.CharField(_('estado'), max_length=255, blank=True, null=True)
    cidade = models.CharField(_('cidade'), max_length=255, blank=True, null=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        null=True
    )
    first_name = models.CharField(
        _('first name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(
        _('last name'), max_length=150, blank=True, null=True)

    email = models.EmailField(_('email'), unique=True)

    is_admin = models.BooleanField(
        _('Administrador'),
        default=False,
        help_text=_('Usuário que possui todas as permissões do sistema.'),
    )
    is_staff = models.BooleanField(
        _('É da equipe'),
        default=False,
        help_text=_('Designa se o usuário pode fazer login no site de administração.'),
    )
    is_active = models.BooleanField(
        _('Ativo'),
        default=True,
        help_text=_(
            'Designa se este usuário deve ser tratado como ativo.' \
            'Desmarque isso em vez de excluir contas.'
        ),
    )

    date_joined = models.DateTimeField(_('data de cadastro'), default=timezone.now)

    dados_publicos_api = models.BooleanField(
        _('Disponibiliza dados do usuário via api pública.'), default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name'
    ]

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')
        permissions = (("view_usuario", "Can view usuários"),)
        # permissão de view foi adicionada como default no django 2.1

    def get_full_name(self):
        '''
        Retorna o nome completo do usuário.
        '''
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        '''
        Retorna o nome do usuário de uma forma 'encurtada'.
        Primeiro e Último nome.
        '''
        nome = self.get_full_name()
        nome_list = nome.split(" ")

        if len(nome_list) > 1:
            return f"{nome_list[0]} {nome_list.pop()}"
        return nome

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Envia um email para o usuário
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.get_full_name()