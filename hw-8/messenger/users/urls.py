from django.urls import path

from users.views import UserRetrieve

urlpatterns = [
    path('<int:pk>/', UserRetrieve.as_view(), name='user_retrieve'),
]
