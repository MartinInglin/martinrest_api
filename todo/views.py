from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = []