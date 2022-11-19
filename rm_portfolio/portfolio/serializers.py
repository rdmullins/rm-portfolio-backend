from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TechStackSerializer(serializers.Serializer):
    class Meta:
        model = TechStack
        fields = ("name",)


class PortfolioProjectSerializer(serializers.Serializer):
    tech_stack = TechStackSerializer()
    class Meta:
        model = PortfolioProject
        fields = "__all__"