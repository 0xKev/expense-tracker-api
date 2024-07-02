from accounts.models import CustomUser
from rest_framework import serializers, permissions
from .models import *
from django.contrib.auth.hashers import make_password

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense
        exclude = ["owner"]


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]


    def create(self, validated_data):
        user = CustomUser.objects.create(
            username = validated_data["username"],
            email = validated_data["email"],
            password = make_password(validated_data["password"])
        )
        return user
    

