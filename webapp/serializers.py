from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Evento

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = ('url', 'username', 'email', 'groups')
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        # fields = ('url', 'name')
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        # fields = ('id', 'name', 'release_date', 'rating', 'category')
        fields = '__all__'
