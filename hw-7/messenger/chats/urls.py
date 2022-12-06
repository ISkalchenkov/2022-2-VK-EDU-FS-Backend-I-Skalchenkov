from django.urls import path

from chats.views import *


urlpatterns = [
    path('', ChatListCreate.as_view(), name='chat_list_create'),
    path('users/<int:user_id>/', UserChatList.as_view(), name='user_chat_list'),
    path('<int:pk>/', ChatRetrieveUpdateDestroy.as_view(), name='chat_retrieve_update_destroy'),

    path('<int:chat_id>/messages/', MessageList.as_view(), name='message_list_create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroy.as_view(), name='message_retrieve_update_destroy'),
    path('messages/<int:pk>/mark_as_read/', MessageMarkAsRead.as_view(), name='message_mark_as_read'),

    path('<int:chat_id>/members/', MemberListCreate.as_view(), name='member_list_create'),
    path('<int:chat_id>/members/<int:member_id>/', MemberDelete.as_view(), name='member_delete'),
]
