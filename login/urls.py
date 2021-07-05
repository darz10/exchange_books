from django.urls import path
from .views import UsersList, ProfileUser


urlpatterns = [
    path('all/', UsersList.as_view(), name="users_list"),
    path('', ProfileUser.as_view(), name="user_profile"),
]
