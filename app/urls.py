from rest_framework import routers

from app.views import LocationViewSet, ProjectViewSet

urlpatterns = []

router = routers.SimpleRouter()
router.register(r'project', ProjectViewSet)
router.register(r'location', LocationViewSet)

urlpatterns += router.urls

app_name = 'app'
