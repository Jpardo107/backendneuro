from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User
#
#
# # Register your models here.
#
#
@admin.register(User)
class UserAdmin(BaseUserAdmin):
     pass
#     # # Agregamos 'deactivated_at' a la sección de fechas importantes
#     # fieldsets = BaseUserAdmin.fieldsets + (
#     #     (('Important dates'), {'fields': ('deactivated_at',)}),
#     # )
#     #
#     # # Mostramos el campo 'deactivated_at' en la vista de lista de usuarios
#     # list_display = BaseUserAdmin.list_display + ('deactivated_at',)
