from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from app.models import Location, Project
from app.serializer import LocationSerializer
from dry_rest_permissions.generics import DRYPermissions


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions, IsAuthenticated)
    queryset = Project.objects.all()
    serializer_class = LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions, IsAuthenticated)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
