import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello World! GraphQL with Django!")

schema = graphene.Schema(query=Query)