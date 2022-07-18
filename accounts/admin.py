"""
.. module:: admin
    :synopsis: De nuestra clase de CustomUser la añadimos para que pueda tener usuarios Admin.

.. moduleauthor:: Roberto Benéitez Vaquero
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


# Register your models here.
class UserAdmin(UserAdmin):
    """
    Clase para CustomUserAdmin. Que nuestro clase CustomUser pueda ser Admin.
    """

    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["email", "username"]


admin.site.register(User, UserAdmin)