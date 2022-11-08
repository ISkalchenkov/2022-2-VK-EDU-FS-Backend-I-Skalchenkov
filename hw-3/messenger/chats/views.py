from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

chats = [
    {'id': 1, 'title': 'Jennifer'},
    {'id': 2, 'title': 'Ivan'},
    {'id': 3, 'title': 'Alexander'},
    {'id': 4, 'title': 'Mary'},
    {'id': 5, 'title': 'Sergey'},
]


@require_http_methods(['GET'])
def chat_list(request):
    return JsonResponse({'chats': chats})


@require_http_methods(['GET'])
def chat_page(request, chat_id):
    requested_chat = next((chat for chat in chats if chat['id'] == chat_id), None)
    if not requested_chat:
        return HttpResponseNotFound()
    return JsonResponse({'chat': requested_chat}, status=201)


@csrf_exempt
@require_http_methods(['POST'])
def create_chat(request):
    new_title = request.POST.get('title', 'default_title')
    new_id = len(chats) + 1
    chats.append({'id': new_id, 'title': new_title})
    return JsonResponse({'created_chat': chats[len(chats) - 1]}, status=201)


@require_http_methods(['GET'])
def homepage(request):
    return render(request, 'index.html')
