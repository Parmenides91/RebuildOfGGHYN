"""
.. module:: views
    :synopsis: Contiene las vistas de la App Accounts.

.. moduleauthor:: Roberto Benéitez Vaquero
"""


from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from accounts.forms import UsuarioTFGCreationForm


class SignUpView(CreateView):
    """
    Registro de nuevos usuarios en el sistema para nuestro UsuarioTFG.
    """

    form_class = UsuarioTFGCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class PerfilUsuario(TemplateView):
    """
    Visualización de los datos principales del UsuarioTFG.
    """

    template_name = 'accounts/perfil_usuario.html'
