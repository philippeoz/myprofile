from django.db import models
from django.utils.translation import ugettext_lazy as _


class UsuarioFilmeFavorito(models.Model):
    """
    Model para filmes favoritos dos usuários
    """
    usuario = models.ForeignKey(
        'Usuario',
        on_delete=models.CASCADE,
        related_name='filmes_favoritos'
    )

    class Meta:
        verbose_name = _('filme favorito do usuário')
        verbose_name_plural = _('usuários - filmes favoritos')
        permissions = (
            ("view_usuario_filme_favorito", "Can view filmes favoritos de usuários"),
        )