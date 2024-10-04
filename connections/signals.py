from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from users.models import User
from connections.models import UserConnections
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(user_logged_in, sender=User)
def log_user_login(sender, request, user, **kwargs):
    print(f'Usuario {user.first_name} ha iniciado sesión')  # Mensaje para depurar
    #creando registro de conexion del usuario
    UserConnections.objects.create(user=user, connection_time=timezone.now())

@receiver(user_logged_out, sender=User)
def log_user_logout(sender, request, user, **kwargs):
    print(f'Usuario {user.first_name} ha cerrado sesión')  # Mensaje para depurar
    #actualizando registro de login con la desconexion al cerrar la sesion
    try:
        connection = UserConnections.objects.filter(user=user).latest('connection_time')
        connection.disconnection_time = timezone.now()
        connection.save()
    except UserConnections.DoesNotExist:
        #Si no hay un registro previo, no hace nada
        pass
