from django.contrib.auth import get_user_model

import graphene
import graphql_social_auth
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):

    class Meta:
        model = get_user_model()


class Mutations(graphene.ObjectType):
    social_auth = graphql_social_auth.SocialAuth.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)


schema = graphene.Schema(query=Query, mutations=Mutations)
