from django.conf import settings
from django.contrib.auth import get_user_model


class FailBackend:
    """
    AuthBackend que possui uma falha de segurança,
    onde o usuário consegue entrar com qualquer senha.
    """
    user_model = get_user_model()

    def authenticate(self, username=None, password=None):
        try:
            return self.user_model.objects.get(email=username)
        except self.user_model.DoesNotExist:
                pass
        return None
    
    def get_user(self, user_id):
        try:
            return self.user_model.objects.get(pk=user_id)
        except self.user_model.DoesNotExist:
            return None 