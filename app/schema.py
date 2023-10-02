import graphene

from .graphql.graph_serializers import TypeSerializer, UserSerializer
from .graphql.graph_api import Mutation
from .graphql.helpers.decorators import require_authenticated_user

from graphene_django.filter import DjangoFilterConnectionField

class Query(graphene.ObjectType):
    all_types = DjangoFilterConnectionField(TypeSerializer)
    all_users = DjangoFilterConnectionField(UserSerializer)
    
    @staticmethod
    def resolve_all_types(self, info, **kwargs):
        return TypeSerializer._meta.model.objects.all()
    
    @staticmethod
    def resolve_all_users(self, info, **kwargs):
        return UserSerializer._meta.model.objects.all()


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

""" query {
  allUsers (isActive: true) {
    edges {
      node {
        id
        databaseId
        username
        email
        isSuperuser
        dateJoined
      }
    }
  }
} """


""" query MyT {
	allTypes (name_Icontains: "T", isActive: true) {
    edges {
      node {
        id
        name
      }
    }
  }
  ...x
}

fragment x on Query {
  allUsers {
    edges {
      node {
        id
      }
    }
  }
} """


"""
query MyT {
	allTypes (user_Username_Istartswith: "A", isActive: true) {
    edges {
      node {
        id
        name
      }
    }
  }
  ...x
}

fragment x on Query {
  allUsers {
    edges {
      node {
        id
      }
    }
  }
}
"""

"""
query MyT {
	allTypes (user_Username_Istartswith: "A", isActive: true) {
    edges {
      node {
        id
        name
        ...u
      }
    }
  }
  ...x
}

fragment x on Query {
  allUsers {
    edges {
      node {
        id
      }
    }
  }
}

fragment u on TypeSerializer {
  user {
    id
    username
  }
}
"""