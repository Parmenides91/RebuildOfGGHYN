"""
.. module:: view
    :synopsis: Contiene las vistas de la App Forecasting.

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
from django.core.exceptions import ValidationError

from accounts.models import UsuarioTFG


class CreateInmueble(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    """
    Vista para creación de un Inmueble.
    """

    model = models.Inmueble
    fields = ('nombre', 'descripcion')

    # def form_valid(self, form):
    #     self.object = form.save(commit = False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)

    def form_valid(self, form):
        self.post = form.save(commit=False)
        self.propietario = form.propietario
        self.object.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.propietario = request.user
            obj.save()
            # prints
            # print('Variable form.is_valid()' + str(form.is_valid()))
            print('Variable obj.user: ' + str(obj.user))
            print('Variable obj.propietario: ' + str(obj.propietario))
            print('Variable obj.propietario: ' + str(obj.nombre))
            print('Variable obj.propietario: ' + str(obj.descripcion))
            return super().form_valid(form)
            # return super(CreateInmueble, self).form_valid(form)
        else:
            print('Estoy en el ELSE de la validación del FORM.')
            print('Valores de datos:')
            # print('Propietario (desde form.)' +form.propietario)
            print('Es Válido (desde form.)' + str(form.is_valid))
            # print('Usuario (desde form.save)' + form.save.user)
            # print('Propietario (desde form.save)' + form.save.propietario)
            # print('Propietario (desde form.save)' + self.propietario)
            raise ValidationError("Algo ha ido mal")
            pass

        # return render(request, 'index.html', context_instance=RequestContext(request))

        # return render(request, 'index.html')
        return null
        return super().form_valid(form)


class InmuebleUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para modificación de los datos de un Inmueble.
    """

    model = models.Inmueble
    fields=['nombre','descripcion']
    template_name_suffix = '_form_update'


# TODO: Debería redirigir al listado de los inmuebles que tenga el usuario. Hay que pasarle por argumento el username (o algo).
class DeleteInmueble(LoginRequiredMixin, DeleteView):
    """
    Vista para eliminación de un Inmueble.
    """

    model = models.Inmueble
    success_url = reverse_lazy('home')
    #success_url = reverse_lazy('forecasting:create_inmueble', kwargs={"username": self.user.username})


class InmuebleDetail(SelectRelatedMixin, DetailView):
    """
    Vista para mostrar los datos de un Inmueble en concreto.
    """

    model = models.Inmueble
    # select_related = ("user",)
    select_related = ("propietario",)

    def get_queryset(self):
        queryset = super().get_queryset()
        # return queryset.filter(user__username__iexact = self.kwargs.get("username"))
        return queryset.filter(propietario__username__iexact=self.kwargs.get("username"))


class UserInmuebles(ListView):
    """
    Vista para listar los Inmuebles de un usuario en concreto.
    """

    model=models.Inmueble
    template_name = "forecasting/inmueble/user_inmueble_list.html"

    def get_queryset(self):
        try:
            self.inmueble_user=UsuarioTFG.objects.get(username__iexact=self.kwargs.get("username"))
        except UsuarioTFG.DoesNotExist:
            raise Http404
        else:
            return self.inmueble_user.inmuebles.all()

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["inmueble_user"]=self.inmueble_user
        return context
