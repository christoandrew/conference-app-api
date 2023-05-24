from django.urls import path, include
from rest_framework_nested import routers

from api.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'conferences', ConferenceViewSet)

# conference_router = routers.NestedSimpleRouter(router, r'conferences', lookup='conference')
# conference_router.register(r'events', views.EventViewSet, basename="events")

urlpatterns = [
    path('', include(router.urls)),
    path('attendees/', AttendeeView.as_view())
]