from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.db.models import Subquery
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from chats.models import Chat, Message, ChatMember
from chats.serializers import ChatSerializer, MessageSerializer, MemberSerializer, \
    ChatUpdateSerializer, MessageUpdateSerializer
from users.models import User


class ChatListCreate(ListCreateAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class UserChatList(ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return Chat.objects.filter(id__in=Subquery(
            user.member_chatmembers.values_list('chat')))


class ChatRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = ChatUpdateSerializer
    queryset = Chat.objects.all()


class MessageList(ListCreateAPIView):
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = get_object_or_404(Chat, id=chat_id)
        return chat.chat_messages.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        chat_id = self.kwargs['chat_id']
        if chat_id != int(request.data['chat']):
            return Response({'detail': 'Id чата в запросе и url отличаются'}, status=status.HTTP_400_BAD_REQUEST)
        member_id = request.data['sender']
        if not ChatMember.objects.filter(chat=chat_id, member=member_id).exists():
            return Response({'detail': 'Отправитель не состоит в чате'}, status=status.HTTP_409_CONFLICT)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MessageRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = MessageUpdateSerializer
    queryset = Message.objects.all()


class MessageMarkAsRead(UpdateAPIView):
    serializer_class = MessageSerializer

    def update(self, request, *args, **kwargs):
        message_id = self.kwargs['pk']
        message = get_object_or_404(Message, id=message_id)
        message.read = True
        message.save()
        return Response({'detail': 'Сообщение помечено прочитанным'})


class MemberListCreate(ListCreateAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = get_object_or_404(Chat, id=chat_id)
        return chat.chat_chatmembers.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        chat_id = self.kwargs['chat_id']
        if chat_id != int(request.data['chat']):
            return Response({'detail': 'Id чата в запросе и url отличаются'}, status=status.HTTP_400_BAD_REQUEST)
        member_id = request.data['member']
        if ChatMember.objects.filter(chat=chat_id, member=member_id).exists():
            return Response({'detail': 'Пользователь уже находится в чате'}, status=status.HTTP_409_CONFLICT)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MemberDelete(DestroyAPIView):
    serializer_class = MemberSerializer

    def get_object(self):
        chat_id = self.kwargs['chat_id']
        member_id = self.kwargs['member_id']
        return get_object_or_404(ChatMember, chat=chat_id, member=member_id)
 

@require_http_methods(['GET'])
def homepage(request):
    return render(request, 'index.html')
