"""
.. module:: views
    :synopsis: Contiene las vistas generales del proyecto (App RebuildOfGGHYN).

.. moduleauthor:: Roberto Benéitez Vaquero
"""

from django.views.generic import TemplateView
from datetime import datetime


# TODO: esta vista debe ir en la app de ACCOUNTS, no aquí.
class AterrizajePage(TemplateView):
    """
    Visualización de la página a la que se les redirige a los usuarios al iniciar y cerrar sesión.
    """

    template_name = 'accounts/aterrizaje.html'


class HomePage(TemplateView):
    """
    Visualización de la página principal del Proyecto.
    """

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # now = datetime.now().__format__('%Y-%m-%d')
        now = datetime.now() # Modificado para poder usar los filtros del paquete Humanize en el index, a la hora de pintarlo.
        context = super().get_context_data(**kwargs)
        context['index_fecha'] = now
        return context

