from django.contrib import admin

from backend.core.models import Usuario
from backend.core.models import UsuarioFilmeFavorito

# Register your models here.
admin.site.register(Usuario)
admin.site.register(UsuarioFilmeFavorito)