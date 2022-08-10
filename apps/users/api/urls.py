from django.urls import path

from apps.users.api.api import UserAPIView, user_api_view

urlpatterns = [
    # path('usuario/', UserAPIView.as_view(), name='usuario_api') # class based
    path('usuario/', user_api_view, name='usuario_api')  # function based
]
