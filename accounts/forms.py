"""
.. module:: forms
    :synopsis: Formulario para los Modelos de la App Accounts.

.. moduleauthor:: Roberto Benéitez Vaquero
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserCreationForm(UserCreationForm):
    """
    Formulario de UserCreationForm para CustomUser.
    """

    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(UserChangeForm):
    """
    Formulario de UserChangeForm para CustomUser.
    """

    class Meta:
        model = User
        fields = ("username", "email")





# class UserCreateForm(UserCreationForm):
#     class Meta:
#         fields = ("username", "email", "password1", "password2")
#         model = get_user_model()
#
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields["username"].label = "Display name"
#             self.fields["email"].label = "Email address"