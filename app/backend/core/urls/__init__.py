from django.urls import path
from django.urls import include

from backend.core.views import RegisterView

from backend.core.urls import profile as profile_urls

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('profile/', include(profile_urls)),
]