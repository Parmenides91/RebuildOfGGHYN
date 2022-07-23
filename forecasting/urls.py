"""
.. module:: urls
    :synopsis: Contiene los mapeos de URLs de la App Forecasting.

.. moduleauthor:: Roberto Benéitez Vaquero
"""


from django.urls import path
from forecasting.views import CreateInmueble, InmuebleDetail, InmuebleUpdateView, DeleteInmueble, UserInmuebles


app_name = 'forecasting'

urlpatterns = [
    # URLs para Inmueble
    path('by/<username>/inmueble/', UserInmuebles.as_view(template_name='inmueble/'), name='for_user_inmuebles'),
    path('by/<username>/inmueble/new/', CreateInmueble.as_view(), name='create_inmueble'),
    path('by/<username>/inmueble/<int:pk>/', InmuebleDetail.as_view(), name='single_inmueble'),
    path('by/<username>/inmueble/edit/<int:pk>/', InmuebleUpdateView.as_view(), name='edit_inmueble'),
    path('by/<username>/inmueble/delete/<int:pk>/', DeleteInmueble.as_view(), name="delete_inmueble"),
]