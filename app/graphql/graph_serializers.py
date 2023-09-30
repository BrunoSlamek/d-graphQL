from graphene_django import DjangoObjectType
from ..models import Type


class TypeSerializer(DjangoObjectType):
    class Meta:
        model = Type
        fields = ('id', 'name')
