from django.db import models
from users.models import User
from django.utils import timezone

class UserConnections(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    connection_time = models.DateTimeField(default=timezone.now)
    disconnection_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} - {self.connection_time}'

