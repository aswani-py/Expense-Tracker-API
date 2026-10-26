from django.shortcuts import render
from expenseApp.serializers import UserSerializer,ExpenseSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from expenseApp.models import Expense
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
class UserCreateView(CreateAPIView):
    serializer_class=UserSerializer

    def perform_create(self, serializer):
        return User.objects.create_user(**serializer.validated_data)


class ExpenseCreateListView(CreateAPIView,ListAPIView):
    serializer_class=ExpenseSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        return serializer.save(owner=user)

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)


    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
        
    ]

    filterset_fields=['category','payment']
    search_fields=['title']
    ordering_fields=['amount','created_at']
    
class ExpenseRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=ExpenseSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=Expense.objects.all()
    lookup_field="id"


