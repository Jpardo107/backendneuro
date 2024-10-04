from rest_framework import generics
from connections.models import UserConnections
from connections.api.serializer import UserConnectionSerializer

class UserConnectionListView(generics.ListAPIView):
    queryset = UserConnections.objects.all()
    serializer_class = UserConnectionSerializer