from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import *
from django.http.response import Http404
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer
    http_method_names = ["get", "post"]