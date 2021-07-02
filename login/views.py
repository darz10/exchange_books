from login.models import Profile
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Profile
from .serializers import UserListSerializer



class UsersList(ListCreateAPIView):
    serializer_class = UserListSerializer
    queryset = Profile.objects.all()
    