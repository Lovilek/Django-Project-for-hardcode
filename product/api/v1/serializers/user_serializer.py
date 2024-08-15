from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import Subscription

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""



    class Meta:
        model = User
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    user = serializers.StringRelatedField(read_only=True)
    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Subscription
        fields = ('id', 'user', 'course', 'start_date')


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
