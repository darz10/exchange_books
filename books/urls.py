from django.urls import path
from .views import CreateCommenntView, ProfileView, DetailBookView, DeleteBook

urlpatterns = [
    # path('', include('exchange.urls')), //TODO главной страницей будет список посделних добавленных книг каждого пользователя с сортировкой по рейтингу
    path('books/', ProfileView.as_view(), name='profile'),
    path('book/<int:pk>/', DetailBookView.as_view(), name='detail_book'),
    path('delete_books/', DeleteBook.as_view(), name='bulk_delete_books '),
    path('create_comment/', CreateCommenntView.as_view(), name='create_comment'),
]
