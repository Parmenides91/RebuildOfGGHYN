"""
.. module:: models
    :synopsis: Contiene los modelos de la App Forecasting. Modelos que contiene: · Inmueble.

.. moduleauthor:: Roberto Benéitez Vaquero
"""
# TODO: el comentario del listado de los modelos en este fichero para Sphinx debe ir en multilinea.


from django.db import models
from django.urls import reverse

from accounts.models import UsuarioTFG


class Inmueble(models.Model):
    """
    Clase para Inmueble. Recoge la información principal de la vivienda de un usuario.
    """

    propietario = models.ForeignKey(UsuarioTFG, on_delete=models.CASCADE, related_name='inmuebles')
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=255, blank=True) # TODO: cambiar este campo a un textField
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("forecasting:single_inmueble", kwargs={"username": self.propietario.username, "pk": self.pk})