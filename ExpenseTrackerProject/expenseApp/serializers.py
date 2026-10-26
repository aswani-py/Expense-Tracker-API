from rest_framework import serializers
from django.contrib.auth.models import User
from expenseApp.models import Expense


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

class ExpenseSerializer(serializers.ModelSerializer):
    owner=UserSerializer(read_only=True)
    class Meta:
        model=Expense
        fields='__all__'
        read_only_fields=['id','created_at']