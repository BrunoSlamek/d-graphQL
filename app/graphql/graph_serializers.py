from graphene_django import DjangoObjectType
from ..models import Type

from django.contrib.auth.models import User


class TypeSerializer(DjangoObjectType):
    class Meta:
        model = Type
        fields = ('id', 'name')


class UserSerializer(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
