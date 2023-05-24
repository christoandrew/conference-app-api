import grpc
from lib.grpc import attendee_service_pb2_grpc
from api.models import *
from api.serializers import *
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets, views
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConferenceViewSet(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    # permission_classes = [permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        conference_id = self.kwargs["conference_pk"]
        return Event.objects.filter(conference=conference_id)


class AttendeeView(views.APIView):
    permission_classes = []

    def get(self, request, format=None):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = attendee_service_pb2_grpc.AttendeesStub(channel)
            attendees = stub.GetConferenceAttendees(attendee_service_pb2.AttendeesRequest(conference_id=1))
            data = AttendeeProtoSerializer(attendees, many=True).data
        return Response(data)
