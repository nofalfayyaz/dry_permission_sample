from rest_framework import serializers

from app.models import Location, Project
from dry_rest_permissions.generics import DRYPermissionsField


class LocationSerializer(serializers.ModelSerializer):
    permissions = DRYPermissionsField()

    class Meta:
        model = Location
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    permissions = DRYPermissionsField()

    class Meta:
        model = Project
        fields = '__all__'
