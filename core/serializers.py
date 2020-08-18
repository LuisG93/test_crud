from .models import User
from rest_framework.serializers import ModelSerializer

############################################################
#Serializers for User CRUD
############################################################
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'address',
            'country',
            'postal_code',
            'studies',
            'occupation',
        )