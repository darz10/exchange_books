from django.db.models.query_utils import Q
from rest_framework.views import APIView, Response
from .models import Room, Exchange_chat
from rest_framework import permissions


class Rooms(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    # def get(self, request):
    #     rooms = Room.objects.filter(Q(creater=request.user) | Q(invited=request.user))
    #     serializer = RoomSerializers(rooms, many=True)
    #     return Response({"data": serializer.data})

    def post(self, request):
        Room.objects.create(creater=request.user)
        return Response(status=201)


class Dialog(APIView):
    """Диалог чата, сообщение"""
    permission_classes = [permissions.IsAuthenticated, ]
   
    # def get(self, request):
    #     room = request.GET.get("room")
    #     chat = Exchange_chat.objects.filter(room=room)
    #     serializer = ChatSerializers(chat, many=True)
    #     return Response({"data": serializer.data})

    # def post(self, request):
        
    #     dialog = ChatPostSerializers(data=request.data)
    #     if dialog.is_valid():
    #         dialog.save(user=request.user)
    #         return Response(status=201)
    #     else:
    #         return Response(status=400)