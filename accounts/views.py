"""
.. module:: views
    :synopsis: Contiene todas las vistas de la app accounts.

.. moduleauthor:: Roberto Benéitez Vaquero
"""


from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


# # Para Iniciar Sesión con el usuario genérico de Django, pero lo estoy sustituyendo por uno custom. Esto quedará obsoleto si lo otro funciona.
# class SignUp(CreateView):
#     """
#     Registro de nuevos usuarios en el sistema.
#     """
#
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy("login")
#     template_name = "accounts/signup.html"


class SignUpView(CreateView):
    """
    Registro de nuevos usuarios en el sistema para nuestro CustomUser.
    """

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


# Mostrar la información de cuenta del usuario
class PerfilUsuario(TemplateView):
    """
    Muestra de los datos que se poseen en el sistema relativos al usuario.
    """

    template_name = 'accounts/perfil_usuario.html'
