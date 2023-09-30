import graphene
from ..models import Type


class CreateType(graphene.Mutation):
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    @staticmethod
    def mutate(self, info, name):
        
        if Type.objects.filter(name=name, is_active=True).exists():
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
        
        if not Type.objects.filter(id=type_id, is_active=True).exists():
            return Exception('Do not exist!')
        
        Type.objects.filter(id=type_id).update(is_active=False)
        return DeleteType(success=True)


class Mutation(graphene.ObjectType):
    create_type = CreateType.Field()
    delete_type = DeleteType.Field()
