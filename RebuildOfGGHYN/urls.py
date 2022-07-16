"""RebuildOfGGHYN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import django


from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from . import views


def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

def custom_server_error(request):
    return django.views.defaults.server_error(request)

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('admin/', admin.site.urls),
    # path('test/', views.TestPage.as_view(), name="test"),
    # path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('bienvenida/', views.BienvenidaPage.as_view(), name="bienvenida"),
    path('despedida/', views.DespedidaPage.as_view(), name="despedida"),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    # path('forecasting/', include("forecasting.urls", namespace="forecasting")),

    # URLs para errores
    path("404/", custom_page_not_found), # sólo visible si DEBUG = False
    path("500/", custom_server_error), # sólo visible si DEBUG = False
]



# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls))
#     ] + urlpatterns
