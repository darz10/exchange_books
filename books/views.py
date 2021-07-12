from rest_framework import filters
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response
from books.serializers import BookSerializer, CreateCommentSerializer
from .models import Book, Comment


class ProfileView(ListCreateAPIView):
    """Вывод списка книг"""    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user', 'name_book', 'author', 'hashtag']
    # permission_classes = [permissions.IsAuthenticated]

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
    # permission_classes = [permissions.IsAuthenticated]


class CreateCommenntView(ListCreateAPIView):
    """Создание коментариев"""

    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DeleteBook(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Book.objects.all()


    def delete(self, request):
        ids = request.data['ids']
        Book.objects.filter(id__in=ids).delete()
        return ids # //TODO массовое удаление 