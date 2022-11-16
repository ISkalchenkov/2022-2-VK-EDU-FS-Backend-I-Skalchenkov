from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime


chats = [
    {
        'id': 1,
        'title': 'Jennifer',
        'creator': 'Ivan',
        'chat_type': 'dialog',
        'created_at': '14-11-2022 12:16',
        'last_update': '14-11-2022 13:33',
    },
    {
        'id': 2,
        'title': 'VK Fullstack',
        'creator': 'Administrator',
        'chat_type': 'group',
        'created_at': '14-11-2022 22:11',
        'last_update': '14-11-2022 22:22',
    },
]


@require_http_methods(['GET'])
def chat_list(request):
    return JsonResponse({'chats': chats})


@require_http_methods(['GET'])
def chat_page(request, chat_id):
    requested_chat = next((chat for chat in chats if chat['id'] == chat_id), None)
    if not requested_chat:
        return HttpResponseNotFound()
    return JsonResponse({'chat': requested_chat})


@csrf_exempt
@require_http_methods(['POST'])
def create_chat(request):
    title = request.POST.get('title')
    id = len(chats) + 1
    creator = request.POST.get('creator')
    chat_type = request.POST.get('chat_type')
    created_at = datetime.now().strftime('%d-%m-%Y %H:%M')
    last_update = created_at
    chats.append(
        {
            'id': id,
            'title': title,
            'creator': creator,
            'chat_type': chat_type,
            'created_at': created_at,
            'last_update': last_update,
        })
    return JsonResponse({'created_chat': chats[len(chats) - 1]}, status=201)


@require_http_methods(['GET'])
def homepage(request):
    return render(request, 'index.html')
