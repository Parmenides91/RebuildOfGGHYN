"""
.. module:: models
    :synopsis: Contiene la clase UsuarioTFG, dentro de la App Accounts, que son los usuarios básicos del sistema. Se parte de "AbstractUser" (que parte de AbstractBaseUser (complejo)) que es sencilla de usar.

.. moduleauthor:: Roberto Benéitez Vaquero
"""


from django.contrib.auth.models import AbstractUser
from django.db import models


class UsuarioTFG(AbstractUser):
    """
    Clase para UsuarioTFG. Será el Usuario que se use en la plataforma.
    """

    # username = models.CharField(max_length=30, unique=True)
    # email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    # firstName = models.CharField(max_length=30)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.username