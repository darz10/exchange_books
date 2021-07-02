from django.db import models
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response
from books.serializers import BookSerializer, CreateCommentSerializer, UserSerializer
from .models import Book, Comment
from django.db.models import Q



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

    def get(self, request):
        """Вывод 15 последних добавленных книг"""

        books = self.get_queryset().order_by('-created_at')[:15]
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailBookView(RetrieveUpdateDestroyAPIView):
    """Детали определенной книги"""
        
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CreateCommenntView(ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
