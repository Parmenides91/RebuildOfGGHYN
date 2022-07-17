"""
.. module:: admin
    :synopsis: De nuestra clase de CustomUser la añadimos para que pueda tener usuarios Admin.

.. moduleauthor:: Roberto Benéitez Vaquero
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    """
    Clase para CustomUserAdmin. Que nuestro clase CustomUser pueda ser Admin.
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]


admin.site.register(CustomUser, CustomUserAdmin)