"""
Django admin page for theming models
"""
from django.contrib import admin

from .models import Location, Project, User


class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
