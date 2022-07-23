"""
.. module:: forms
    :synopsis: Formularios para los Modelos de la App Accounts.

.. moduleauthor:: Roberto Benéitez Vaquero
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import UsuarioTFG


class UsuarioTFGCreationForm(UserCreationForm):
    """
    Formulario de UserCreationForm para UsuarioTFG.
    """

    class Meta:
        model = UsuarioTFG
        fields = ("username", "email")


class UsuarioTFGChangeForm(UserChangeForm):
    """
    Formulario de UserChangeForm para UsuarioTFG.
    """

    class Meta:
        model = UsuarioTFG
        fields = ("username", "email")

