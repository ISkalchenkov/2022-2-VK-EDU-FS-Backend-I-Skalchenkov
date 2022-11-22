from django.urls import path

from chats.views import chat_list, chat_detail, chat_create, chat_edit, chat_delete
from chats.views import message_list, message_create, message_detail, message_edit, message_delete


urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<int:chat_id>/', chat_detail, name='chat_detail'),
    path('create/', chat_create, name='chat_create'),
    path('edit/<int:chat_id>/', chat_edit, name='chat_edit'),
    path('delete/<int:chat_id>/', chat_delete, name='chat_delete'),

    path('<int:chat_id>/messages/', message_list, name='message_list'),
    path('messages/<int:message_id>/', message_detail, name='message_detail'),
    path('messages/create/', message_create, name='message_create'),
    path('messages/edit/<int:message_id>/', message_edit, name='message_edit'),
    path('messages/delete/<int:message_id>/', message_delete, name='message_delete'),

]
