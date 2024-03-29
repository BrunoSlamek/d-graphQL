import graphene
from ..models import Type
from django.contrib.auth.models import User


class CreateType(graphene.Mutation):
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    @staticmethod
    def mutate(self, info, name):

        if Type.objects.filter(name=name, is_active=True).exists():
            return Exception('Already exists!')
        
        obj = Type(name=name, user=User.objects.get(id=1))
        obj.save()

        return CreateType(name=obj.name)


class UpdateType(graphene.Mutation):
    name = graphene.String()

    class Arguments:
        type_id = graphene.ID(required=True)
        name = graphene.String(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(self, info, type_id, name):
        if not Type.objects.filter(id=type_id, is_active=True).exists():
            return Exception('Type ID DoesNotExist')
        
        Type.objects.filter(id=type_id, is_active=True).update(name=name)
        return UpdateType(success=True)


class DeleteType(graphene.Mutation):
    class Arguments:
        type_id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, type_id):
        
        if not Type.objects.filter(id=type_id, is_active=True).exists():
            return Exception('Do not exist!')
        
        Type.objects.filter(id=type_id).update(is_active=False)
        return DeleteType(success=True)


class Mutation(graphene.ObjectType):
    create_type = CreateType.Field()
    UpdateType = UpdateType.Field()
    delete_type = DeleteType.Field()
