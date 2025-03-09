from .models import Todo 
from . import serializers
from rest_framework import viewsets 
from django.contrib.auth import get_user_model

User = get_user_model() 

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer