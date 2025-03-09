from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']    

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = models.Todo
        fields = ['url', 'task', 'id', 'created_at', 'author', 'marked']
