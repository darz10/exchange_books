from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView, Response
from .models import Profile
from .serializers import UserListSerializer



class UsersList(ListCreateAPIView):
    serializer_class = UserListSerializer
    queryset = Profile.objects.all()
    

class ProfileUser(ListCreateAPIView):
    serializer_class = UserListSerializer
    
    def get_queryset(self):
        user = self.request.user
        return user

