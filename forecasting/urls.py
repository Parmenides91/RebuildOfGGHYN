"""
"""

from django.urls import path
from . import views # TODO: ponerlo como from forecasting import views. Y ver así que si casca algo es porque está fuera del views que importo.

from django.conf import settings


app_name='forecasting'

urlpatterns = [
    # URLs para Inmueble
    path('by/<username>/inmueble/', views.UserInmuebles.as_view(template_name='inmueble/'), name='for_user_inmuebles'),
    path('by/<username>/inmueble/new/', views.CreateInmueble.as_view(), name='create_inmueble'),
    path('by/<username>/inmueble/<int:pk>/', views.InmuebleDetail.as_view(), name='single_inmueble'),
    path('by/<username>/inmueble/edit/<int:pk>/', views.InmuebleUpdateView.as_view(), name='edit_inmueble'),
    path('by/<username>/inmueble/delete/<int:pk>/', views.DeleteInmueble.as_view(), name="delete_inmueble"),
]