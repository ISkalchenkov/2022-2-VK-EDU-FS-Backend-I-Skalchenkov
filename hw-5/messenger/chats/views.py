import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from chats.models import Chat, ChatType, Message
from users.models import User

def chat_serialize(chat: Chat):
    serialized_chat = {
        'id': chat.pk,
        'title': chat.title,
        'description': chat.description,
        'chat_type_id': chat.chat_type.pk,
        'creator_id': chat.creator.pk,
        'created_at': chat.created_at,
    }
    return serialized_chat


def message_serialize(message: Message):
    serialized_message = {
        'id': message.pk,
        'body': message.body,
        'created_at': message.created_at,
        'sender_id': message.sender.pk,
        'chat_id': message.chat.pk,
    }
    return serialized_message


@require_http_methods(['POST'])
def chat_create(request):
    data = json.loads(request.body)
    data['creator'] = User.objects.get(id=data['creator'])
    data['chat_type'] = ChatType.objects.get(id=data['chat_type'])
    chat = Chat.objects.create(**data)
    created_chat = chat_serialize(chat)
    return JsonResponse({'created_chat': created_chat}, status=201)


@require_http_methods(['GET'])
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    required_chat = chat_serialize(chat)
    return JsonResponse({'chat': required_chat}, status=200)


@require_http_methods(['GET'])
def chat_list(request):
    chats = Chat.objects.all()
    ch = [
        chat_serialize(chat) for chat in chats
    ]
    return JsonResponse({'chats': ch}, status=200)


@require_http_methods(['PATCH'])
def chat_edit(request, chat_id):
    data = json.loads(request.body)
    get_object_or_404(Chat, id=chat_id)
    Chat.objects.filter(id=chat_id).update(**data)
    edited_chat = chat_serialize(Chat.objects.get(id=chat_id))
    return JsonResponse({'edited_chat': edited_chat}, status=200)


@require_http_methods(['DELETE'])
def chat_delete(request, chat_id):
    chat_to_delete = get_object_or_404(Chat, id=chat_id)
    deleted_chat = chat_serialize(chat_to_delete)
    chat_to_delete.delete()
    return JsonResponse({'deleted_chat': deleted_chat}, status=200)


@require_http_methods(['POST'])
def message_create(request):
    data = json.loads(request.body)
    data['sender'] = User.objects.get(id=data['sender'])
    data['chat'] = Chat.objects.get(id=data['chat'])
    message = Message.objects.create(**data)
    created_message = message_serialize(message)
    return JsonResponse({'created_message': created_message}, status=201)


@require_http_methods(['GET'])
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    required_message = message_serialize(message)
    return JsonResponse({'message': required_message}, status=200)


@require_http_methods(['GET'])
def message_list(request, chat_id):
    get_object_or_404(Chat, id=chat_id)
    chat_messages = Message.objects.filter(chat=chat_id)
    chat_messages = [
        message_serialize(message) for message in chat_messages
    ]
    return JsonResponse({'chat_messages': chat_messages}, status=200)


@require_http_methods(['PATCH'])
def message_edit(request, message_id):
    data = json.loads(request.body)
    get_object_or_404(Message, id=message_id)
    Message.objects.filter(id=message_id).update(**data)
    edited_message = message_serialize(Message.objects.get(id=message_id))
    return JsonResponse({'edited_message': edited_message}, status=200)


@require_http_methods(['DELETE'])
def message_delete(request, message_id):
    message_to_delete = get_object_or_404(Message, id=message_id)
    deleted_message = message_serialize(message_to_delete)
    message_to_delete.delete()
    return JsonResponse({'deleted_message': deleted_message}, status=200)


@require_http_methods(['GET'])
def homepage(request):
    return render(request, 'index.html')
