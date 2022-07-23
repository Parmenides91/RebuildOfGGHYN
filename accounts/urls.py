"""
.. module:: urls
    :synopsis: Contiene los mapeos de URLs de la App Accounts.

.. moduleauthor:: Roberto Benéitez Vaquero
"""


from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import SignUpView, PerfilUsuario


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    path('signup/', SignUpView.as_view(), name="signup"),

    path('<username>', PerfilUsuario.as_view(), name = "perfil_usuario"),
]