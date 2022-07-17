"""
.. module:: view
    :synopsis: Contiene todas las vistas de la app forecasting.

.. moduleauthor:: Roberto Benéitez Vaquero
"""


from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404
from . import models
from . import forms
from .forms import InmuebleForm
from django.conf import settings

from accounts.models import CustomUser

# from django.contrib.auth import get_user_model
# User = get_user_model()


# Crear un nuevo inmueble
class CreateInmueble(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    """
    Creación de un Inmueble
    """

    model = models.Inmueble
    fields = ('nombre', 'descripcion')

    # def form_valid(self, form):
    #     self.object = form.save(commit = False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)


# Modificar un inmueble existente
class InmuebleUpdateView(LoginRequiredMixin, UpdateView):
    """
    Modificación de los datos de un Inmueble.
    """

    model = models.Inmueble
    fields=['nombre','descripcion']
    template_name_suffix = '_form_update'


# Eliminar un inmueble
# """
#     Esta vista requiere atención:
#     - Debería redirigir al listado de los inmuebles que tenga el usuario. Hay que pasarle por argumento el username
# """
class DeleteInmueble(LoginRequiredMixin, DeleteView):
    """
    Eliminación de un Inmueble
    """

    model = models.Inmueble
    success_url = reverse_lazy('home')
    #success_url = reverse_lazy('forecasting:create_inmueble', kwargs={"username": self.user.username})


#muestra un inmueble individual
class InmuebleDetail(SelectRelatedMixin, DetailView):
    """
    Muestra de los datos para un Inmueble en concreto.
    """

    model = models.Inmueble
    select_related = ("user",)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get("username"))

# Listado de Inmuebles para un usuario
class UserInmuebles(ListView):
    """
    Listado de los Inmuebles para un usuario en concreto.
    """

    model=models.Inmueble
    template_name = "forecasting/inmueble/user_inmueble_list.html"

    def get_queryset(self):
        try:
            self.inmueble_user=CustomUser.objects.get(username__iexact=self.kwargs.get("username"))
        except CustomUser.DoesNotExist:
            raise Http404
        else:
            return self.inmueble_user.inmuebles.all()

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["inmueble_user"]=self.inmueble_user
        return context
