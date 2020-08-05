from django.contrib.auth.models import User, Group
from rest_framework import serializers
from chess_engine.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ChessGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GamePersistentData
        fields = ['id', 'data']
#
# class RotemSerializer():
#     class Meta:
#         model = 'GamePersistentData'
#         fields = ['fen']