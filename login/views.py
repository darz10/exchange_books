from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import Profile
from .serializers import UserListSerializer


class UsersList(ListCreateAPIView):
    """Список всех зарегистрированных пользователей и их книги"""
    serializer_class = UserListSerializer
    queryset = Profile.objects.all()


class ProfileUser(APIView):
    """Профиль текущего пользователя"""

    def get(self, request):
        try:
            user = self.request.user.username
            query = Profile.objects.get(username=user)
            serializer = UserListSerializer(query)
        except:
            raise Http404
        return Response(serializer.data)
