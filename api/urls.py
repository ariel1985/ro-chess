# from django.urls import include, path
from rest_framework import routers
from api import views
from django.conf.urls import url, include

# from api.views import RotemTestAPI

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'games', views.GameViewSet)
# router.register(r'^rotem/(?P<pk>[0-9]+)$', views.RotemTestAPI)
# router.register(r'rotem', RotemTestAPI.as_view())


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]