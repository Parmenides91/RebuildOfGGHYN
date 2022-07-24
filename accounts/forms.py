"""
.. module:: forms
    :synopsis: Formularios para los Modelos de la App Accounts.

.. moduleauthor:: Roberto Benéitez Vaquero
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from accounts.models import UsuarioTFG


class UsuarioTFGCreationForm(UserCreationForm):
    """
    Formulario de UserCreationForm para UsuarioTFG.
    """

    verify_email = forms.EmailField(label = 'Email address again')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise ValidationError("La dirección de email debe coincidir.")
        else:
            pass

    class Meta:
        model = UsuarioTFG
        fields = ("username", "email", 'verify_email')


class UsuarioTFGChangeForm(UserChangeForm):
    """
    Formulario de UserChangeForm para UsuarioTFG.
    """

    class Meta:
        model = UsuarioTFG
        fields = ("username", "email")

