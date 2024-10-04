from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)

    # Sobrescribimos la funcion save para manejar la fecha de desactivación
    def save(self, *args, **kwargs):
        # Si el usuario se está desactivando (is_active pasa a False)
        if not self.is_active and not self.deactivated_at:
            self.deactivated_at = timezone.now()  # Registra la fecha actual
        # Si el usuario se reactiva, limpiamos la fecha de desactivación
        elif self.is_active:
            self.deactivated_at = None

        # Llama a la funcion save original
        super().save(*args, **kwargs)