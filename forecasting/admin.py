"""
.. module:: admin
    :synopsis: Se permite que los modelos de la App de Forecasting sean gestionables desde desde ADMINISTRACIÓN de Django.

.. moduleauthor:: Roberto Benéitez Vaquero
"""
# TODO: listado para Sphinx.


from django.contrib import admin
from forecasting.models import Inmueble

admin.site.register(Inmueble)