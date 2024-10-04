from rest_framework import serializers
from connections.models import UserConnections
from users.api.serializer import UserConnSerializer


class UserConnectionSerializer(serializers.ModelSerializer):
    user = UserConnSerializer(read_only=True) #anidando los datos del usuario
    class Meta:
        model = UserConnections
        fields = ['id','user', 'connection_time', 'disconnection_time']