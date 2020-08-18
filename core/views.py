from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import User
from .serializers import UserSerializer

############################################################
#REST API for User
############################################################
class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    #Enable filters
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('username', 'first_name', 'last_name', 'studies', 'occupation')