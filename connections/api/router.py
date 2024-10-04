from django.urls import path
from connections.api.views import UserConnectionListView

urlpatterns = [
    path('connections/', UserConnectionListView.as_view(), name='user-connections')
]