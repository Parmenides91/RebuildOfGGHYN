"""
.. module:: admin
    :synopsis: Se permite que la UsuarioTFG sea gestionable desde ADMINISTRACIÓN de Django y puedan ser administradores.

.. moduleauthor:: Roberto Benéitez Vaquero
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import UsuarioTFGCreationForm, UsuarioTFGChangeForm
from accounts.models import UsuarioTFG


class UsuarioTFGAdmin(UserAdmin):
    """
    Clase para que UsuarioTFG pueda ser administrador (no estoy seguro de qué cojones hace esta clase o si hace algo, la verdad :\ )
    """

    add_form = UsuarioTFGCreationForm
    form = UsuarioTFGChangeForm
    model = UsuarioTFG
    list_display = ["email", "username"]


admin.site.register(UsuarioTFG, UsuarioTFGAdmin)