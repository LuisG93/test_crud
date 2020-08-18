from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import UserViewSet
#drf_yasg
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

#Define router object
router = DefaultRouter()
router.register(r'users', UserViewSet)

core_api_patterns = router.urls

#Define schema for the api documentation
schema_view = get_schema_view(
   openapi.Info(
      title="e-learning API",
      default_version='v1',
      description="This is the api documentation for a test api",
      contact=openapi.Contact(email="luis.garcia.93.e@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

#Create an array with the urls
api_patterns = [
   #Core views
   url(r'^', include(core_api_patterns)),
   #Token
   url(r'^token-auth/', TokenObtainPairView.as_view()),
   url(r'^token-refresh/', TokenRefreshView.as_view()),
   url(r'^token-verify/', TokenVerifyView.as_view()),
   #docs
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]