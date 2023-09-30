import graphene

from .models import Type

from .graphql.graph_serializers import TypeSerializer, UserSerializer
from .graphql.graph_api import Mutation
from .graphql.helpers.decorators import require_authenticated_user

from django.contrib.auth.models import User


class Query(graphene.ObjectType):
    types = graphene.List(TypeSerializer)
    type_by_id = graphene.Field(TypeSerializer, type_id=graphene.ID())
    users = graphene.List(UserSerializer)

    @staticmethod
    # @require_authenticated_user
    def resolve_types(root, info):
        print(info.context.user)
        return Type.return_all_active()

    @staticmethod
    @require_authenticated_user
    def resolve_type_by_id(root, info, type_id):
        return Type.get_by_id(type_id=type_id)

    @staticmethod
    @require_authenticated_user
    def resolve_users(root, info):
        return User.objects.all()

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

""" query {
  types {
    id
    name
  }
  users {
    id
    username
    isSuperuser
  }
} """


""" mutation {
  UpdateType(typeId: 6, name: "Try2") {
    success
  }
}
 """

"""
query {
  types {
    id
    name
    user {
      id
      usernameT: username
      root: isSuperuser
      dateJoined
    }
  }
}
"""