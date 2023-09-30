import graphene

from .models import Type

from .graphql.graph_serializers import TypeSerializer
from .graphql.graph_api import Mutation


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


""" mutation {
  createType(
    name: "Bruno"
  ) {
    name
  }
} """

""" mutation {
  deleteType(typeId: 1) {
    success
  }
} """