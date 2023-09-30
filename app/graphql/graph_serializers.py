from graphene_django import DjangoObjectType
from ..models import Type

from django.contrib.auth.models import User


class UserSerializer(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class TypeSerializer(DjangoObjectType):
    user = UserSerializer()

    class Meta:
        model = Type
        fields = ('id', 'name', 'user')
