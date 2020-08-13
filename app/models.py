from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    company = models.CharField(max_length=150, blank=True)

class Location(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    address = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

    @staticmethod
    def has_read_permission(request):
        return request.user.has_perm('app.view_location')

    def has_object_read_permission(self, request):
        return request.user.has_perm('app.view_location')

    @staticmethod
    def has_write_permission(request):
        return request.user.has_perm('app.change_location')

    @staticmethod
    def has_create_permission(request):
        return request.user.has_perm('app.add_location')


class Project(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    @staticmethod
    def has_read_permission(request):
        return request.user.has_perm('app.view_project')

    def has_object_read_permission(self, request):
        return request.user.has_perm('app.view_project')

    @staticmethod
    def has_write_permission(request):
        return request.user.has_perm('app.change_project')

    @staticmethod
    def has_create_permission(request):
        return request.user.has_perm('app.add_project')
