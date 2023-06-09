import graphene
from graphene_django import DjangoObjectType

from .models import Type


# Serializer?
class TypeSerializer(DjangoObjectType):
    class Meta:
        model = Type
        fields = ('id', 'name')


class CreateType(graphene.Mutation):
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    @staticmethod
    def mutate(self, info, name):
        obj = Type(name=name)
        obj.save()

        return CreateType(
            name=obj.name,
        )


class Mutation(graphene.ObjectType):
    create_type = CreateType.Field()


class Query(graphene.ObjectType):
    """ hello = graphene.String(default_value="Hello World! GraphQL with Django!") """
    types = graphene.List(TypeSerializer)
    # type_by_id = graphene.Field(TypeSerializer, name=graphene.String(required=True))
    type_by_id = graphene.Field(TypeSerializer, type_id=graphene.ID())

    @staticmethod
    def resolve_types(root, info):
        return Type.objects.filter()

    @staticmethod
    def resolve_type_by_id(root, info, type_id):
        return Type.objects.get(id=type_id)


schema = graphene.Schema(query=Query, mutation=Mutation)


# mutation {
#   createType(
#    name: "Bruno"
#   ) {
#     name
#   }
# }
