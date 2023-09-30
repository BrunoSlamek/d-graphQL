
from graphql import GraphQLError

def require_authenticated_user(func):
    def wrapper(root, info, *args, **kwargs):
        if info.context.user.is_anonymous:
            raise GraphQLError('Not authenticated')
        return func(root, info, *args, **kwargs)
    return wrapper
