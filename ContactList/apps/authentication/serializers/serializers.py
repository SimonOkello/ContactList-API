from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=4)
    email = serializers.EmailField(max_length=255, min_length=8)
    first_name = serializers.CharField(max_length=255, min_length=4)
    last_name = serializers.CharField(max_length=255, min_length=4)
    password = serializers.CharField(
        max_length=255, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username')
        if not email:
            return None
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': ('Username is taken')})
        elif User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email already exists')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, min_length=4)

    password = serializers.CharField(
        max_length=255, min_length=8, write_only=True)
