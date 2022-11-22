from django.urls import path

from chats.views import *

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
    path('messages/mark_as_read/<int:message_id>/', message_mark_as_read, name='message_mark_as_read'),

    path('members/create/', member_create, name='member_create'),
    path('members/delete/<int:member_id>/<int:chat_id>/', member_delete, name='member_delete'),

]
