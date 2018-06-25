from .usuario import *
from .usuario_filmes import *

from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import update_last_login

def update_first_login(sender, user, **kwargs):
    if user.last_login is None:
        kwargs['request'].session['first_login'] = True
    update_last_login(sender, user, **kwargs)

user_logged_in.disconnect(update_last_login)
user_logged_in.connect(update_first_login)