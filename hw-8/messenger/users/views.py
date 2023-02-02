from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.generics import RetrieveAPIView

from users.models import User
from users.serializers import UserSerializer


class UserRetrieve(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
