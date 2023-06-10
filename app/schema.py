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
        exists = Type.objects.filter(name=name, is_active=True).exists()
        if exists:
            return Exception('Already exists!')
        
        obj = Type(name=name)
        obj.save()

        return CreateType(name=obj.name)
    

class DeleteType(graphene.Mutation):
    class Arguments:
        type_id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, type_id):
        obj = Type.objects.get(id=type_id)
        obj.is_active = False
        obj.save()
        return DeleteType(success=True)


class Mutation(graphene.ObjectType):
    create_type = CreateType.Field()
    delete_type = DeleteType.Field()


class Query(graphene.ObjectType):
    types = graphene.List(TypeSerializer)
    type_by_id = graphene.Field(TypeSerializer, type_id=graphene.ID())

    @staticmethod
    def resolve_types(root, info):
        return Type.objects.filter(is_active=True)

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
