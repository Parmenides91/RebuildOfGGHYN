"""
.. module:: urls
    :synopsis: Contiene todos los mapeos de urls de la app accounts.

.. moduleauthor:: Roberto Benéitez Vaquero
"""


from django.urls import path
from django.contrib.auth import views as auth_views

from . import views # TODO: ponerlo como from forecasting import views. Y ver así que si casca algo es porque está fuera del views que importo.


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('signup/', views.SignUp.as_view(), name="signup"),
    path('signup/', views.SignUpView.as_view(), name="signup"),

    path('<username>',views.PerfilUsuario.as_view(), name = "perfil_usuario"),
]