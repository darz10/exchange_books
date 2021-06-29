from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response
from exchange.serializers import BookSerializer, CreateCommentSerializer, UserSerializer
from .models import Book, Comment
from django.db.models import Q
from django.shortcuts import render


class ProfileView(ListCreateAPIView):
    
    serializer_class = BookSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Book.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailBookView(RetrieveUpdateDestroyAPIView):
    """Детали определенной книги"""
        
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CreateCommenntView(ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer


class TestView(APIView):

    def get(self, request, *args, **kwargs):
        data = [{"color": "black", "name": "white"}, {"color":"yellow", "name": "Jack"}]
        return Response(data)


def index(request):
    return render(request, 'index.html',{})