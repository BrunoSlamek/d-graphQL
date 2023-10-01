from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from ..models import Type
import graphene

from django.contrib.auth.models import User


class UserSerializer(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'id': ['exact'],
            'username': ['exact', 'istartswith'],
            'is_active': ['exact']
        }
        interfaces = (relay.Node, )

    database_id = graphene.Int()

    def resolve_database_id(self, info):
        return self.id


class TypeSerializer(DjangoObjectType):
    user = UserSerializer()

    class Meta:
        model = Type
        fields = ('id', 'name', 'user')
