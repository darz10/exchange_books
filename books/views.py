from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response
from books.serializers import BookSerializer, CreateCommentSerializer
from .models import Book, Comment


class ProfileView(ListCreateAPIView):
    """Вывод списка книг"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name_book', 'author__name_author']
    # permission_classes = [permissions.IsAuthenticated]


class DetailBookView(RetrieveUpdateDestroyAPIView):
    """Детали определенной книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CreateCommenntView(ListCreateAPIView):
    """Создание коментариев"""
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeleteBook(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Book.objects.all()

    def delete(self, request):
        ids = request.data['ids']
        Book.objects.filter(id__in=ids).delete()
        return ids  # //TODO массовое удаление
