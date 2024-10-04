from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Crea un superusuario si no existe'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Cambia estos valores a los que prefieras
        username = 'JaimeP'
        email = 'jdpm2014@gmail.com'
        password = 'Seb@stian133'

        try:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f'Superusuario {username} creado con éxito.'))
            else:
                self.stdout.write(self.style.WARNING(f'El superusuario {username} ya existe.'))
        except IntegrityError:
            self.stdout.write(self.style.WARNING(f'Error creando el superusuario {username}.'))
