"""
.. module:: urls
    :synopsis: Contiene los mapeos generales del proyecto (App RebuildOfGGHYN).

.. moduleauthor:: Roberto Benéitez Vaquero
"""

import django

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from RebuildOfGGHYN.views import HomePage, AterrizajePage

# Vista para Error404
def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

# Vista para Error500
def custom_server_error(request):
    return django.views.defaults.server_error(request)

urlpatterns = [
    # URL para página principal
    path('', HomePage.as_view(), name="home"),

    # URL de acceso al apartado de ADMINISTRACIÓN
    path('admin/', admin.site.urls),

    # URLs para App Accounts
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/aterrizaje/', AterrizajePage.as_view(), name="aterrizaje"), # TODO: esta debería ir en Account, aquí sólo el include

    # URLs para App Forecasting
    path('forecasting/', include("forecasting.urls", namespace="forecasting")),

    # URLs para errores
    path("404/", custom_page_not_found), # sólo visible si DEBUG = False
    path("500/", custom_server_error), # sólo visible si DEBUG = False
]


# Necesitas tener "debug_toolbar" como APP instalada en el settings.py
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls))
#     ] + urlpatterns
