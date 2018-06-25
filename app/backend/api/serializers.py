from rest_framework import serializers

from backend.core.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    filmes_favoritos = serializers.StringRelatedField(many=True)
    foto = serializers.SerializerMethodField()
    foto_miniatura = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = [
            'id',
            'first_name',
            'last_name',
            'foto',
            'foto_miniatura',
            'email',
            'sexo',
            'pais',
            'estado',
            'cidade',
            'filmes_favoritos'
        ]
    
    def get_foto(self, obj):
        if obj.foto:
            return self.context['request'].build_absolute_uri(obj.foto.url)
        return None
    
    def get_foto_miniatura(self, obj):
        if obj.foto_thumbnail:
            return self.context['request'].build_absolute_uri(
                obj.foto_thumbnail.url)
        return None