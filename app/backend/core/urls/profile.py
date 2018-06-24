from django.urls import path
from django.urls import include

from backend.core.views import MyProfilePublicView
from backend.core.views import MyProfileEditView
from backend.core.views import MyProfileSetupView


urlpatterns = [
    path('<int:pk>/public/', MyProfilePublicView.as_view(), name='profile-public'),
    path('<int:pk>/edit/', MyProfileEditView.as_view(), name='profile-edit'),
    path('<int:pk>/setup/', MyProfileSetupView.as_view(), name='profile-setup'),
]
