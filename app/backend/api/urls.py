
from django.urls import path, include

from backend.api.views import UsuarioViewSet



urlpatterns = [
    path('profile/<int:pk>/', UsuarioViewSet.as_view({'get': 'retrieve'})),
]