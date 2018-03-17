
import graphene

from graphene_django import DjangoObjectType

from api.models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class Query(object):
    all_events = graphene.List(EventType)

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()
