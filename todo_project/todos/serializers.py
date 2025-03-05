from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        fields = '__all__'