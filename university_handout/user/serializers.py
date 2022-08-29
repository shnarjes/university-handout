from rest_framework import serializers
from user.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name', 'email')
