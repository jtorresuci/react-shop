from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        # Fields not all because it might contain sensitive information like passwords
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get_isAdmin(self,obj):
        return obj.is_staff

    def get__id(self, obj):
        return obj.id

    # Function to concatenate first_name and last_name
    # @param obj is user object
    # NOTE: function name has to be 'get_{fieldName}' in order to be called
    # Documentation for user object:
    # https://docs.djangoproject.com/en/4.1/ref/contrib/auth/

    def get_name(self, obj):
            name = obj.first_name
            if name == '':
                name = obj.email

            return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    # Returning token for frontend when we serialize our data
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



# NOTE: on serializers
# Serializers allow complex data such as querysets and model instances 
# to be converted to native Python datatypes that can then be easily 
# rendered into JSON, XML or other content types.