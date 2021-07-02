from django.urls import path, include
from .views import UsersList


urlpatterns = [
    path('', UsersList.as_view(), name="users_list"),
]
