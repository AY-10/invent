from api.models import User, Profile
from django.contrib.auth.auth.password_validation import validate_password
from rest_framework.authtoken.models import TokenObtainPairSerializer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.profile._full_name()
        token['email'] = user.email
        token['username'] = user.username
        token['bio'] = user.profile.bio
        token['image'] = user.profile.image
        token['verified'] = user.profile.verified
        return token


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

        def validate(self, attrs):
            if attrs['password1'] != attrs['password2']:
                raise serializers.ValidationError(
                    {"password": "Passwords do not match."})
            return attrs

        def create(self, validated_data):
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
            )
            user.set_password(validated_data['password'])
            user.save()

            return user
