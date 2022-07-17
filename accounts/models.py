"""
.. module:: models
    :synopsis: Contiene la clase usuario que se necesita para el sistema. Se ha creado una nueva clase para Usuario, partiendo de AbstracUser (que a su vez parte de AbstractBaseUser pero que ya trae una configuración básica por defecto para hacerlo más sencillo de usar).

.. moduleauthor:: Roberto Benéitez Vaquero
"""

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils import timezone



# Create your models here.
class CustomUser(AbstractUser):
    """
    Clase para CustomUser. Será el Usuario que se use en la plataforma.
    """
    pass
    # add additional fields in here

    def __str__(self):
        return self.username