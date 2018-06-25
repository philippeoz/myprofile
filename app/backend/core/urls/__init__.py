from django.urls import path
from django.urls import include

from backend.core.views import RegisterView
from backend.core.views import check_first_login

from backend.core.urls import profile as profile_urls

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('', check_first_login, name='profile'),

    path('profile/', include(profile_urls)),
]