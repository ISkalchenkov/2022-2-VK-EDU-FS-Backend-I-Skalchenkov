from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from users.models import User


def user_serialize(user: User):
    serialized_user = {
        'id': user.pk,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'bio': user.bio,
        'location': user.city,
        'phone_number': user.phone_number,
    }
    return serialized_user


@require_http_methods(['GET'])
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    required_user = user_serialize(user)
    return JsonResponse({'user': required_user}, status=200)
