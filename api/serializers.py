from django.contrib.auth.models import User, Group
from django_grpc_framework import proto_serializers
from rest_framework import serializers

from api.models import *
from api import attendee_service_pb2


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conference
        exclude = ["created_at", "updated_at"]

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        exclude = ["created_at", "updated_at"]

class AttendeeProtoSerializer(proto_serializers.ProtoSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    id = serializers.IntegerField()
    age = serializers.IntegerField()

    class Meta:
        proto_class = attendee_service_pb2.Attendee
        fields = ["id", "name", "email", "age"]