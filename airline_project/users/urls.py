from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', registerAPIView.as_view()),
    path('api-token-auth/', LoginAPIView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view())
]