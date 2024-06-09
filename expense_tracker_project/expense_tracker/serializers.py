from accounts.models import CustomUser
from rest_framework import serializers, permissions
from .models import *

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense
        exclude = ["owner"]
        permissions_class = [permissions.IsAuthenticatedOrReadOnly]
