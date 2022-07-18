"""
.. module:: models
    :synopsis: Contiene los modelos necesarios para la app forecasting

.. moduleauthor:: Roberto Benéitez Vaquero
"""

from django.db import models
from django.urls import reverse
# from django.contrib.auth import get_user_model

from accounts.models import CustomUser

# User = get_user_model()

# Create your models here.
class Inmueble(models.Model):
    """
    Clase para Inmueble. Recoge la información principal de la vivienda de un usuario.
    """

    propietario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='inmuebles', default=1)
    # propietario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='inmuebles', null=True)
    # propietario = models.ForeignKey(CustomUser, related_name='inmuebles', on_delete=models.CASCADE(collector=None, field=0, sub_objs=0, using=0))
    # propietario = models.ForeignKey(User, related_name="inmuebles", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("forecasting:single_inmueble", kwargs={"username": self.propietario.username, "pk": self.pk})