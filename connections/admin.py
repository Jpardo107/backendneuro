from django.contrib import admin
from connections.models import UserConnections

# Registrar el modelo UserConnection en el admin
@admin.register(UserConnections)
class UserConnectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'connection_time', 'disconnection_time')  # Campos que se mostrarán en la lista
    search_fields = ('user__username',)  # Añadir barra de búsqueda por nombre de usuario
    list_filter = ('connection_time', 'disconnection_time')  # Añadir filtros laterales para tiempos de conexión
