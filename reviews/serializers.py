from rest_framework import serializers
from reviews.models import Critico

class CriticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Critico
        fields = ['id', 'nome', 'foto', 'email', 'descricao', 'review', 'video']