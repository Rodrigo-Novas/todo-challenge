from rest_framework import serializers
from list.models import Lista

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = ['id', 'description', 'status', 'creation_date']