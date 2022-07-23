"""
.. module:: forms
    :synopsis: Formulario para los Modelos de la App Forecasting. Formularios que contiene: · __listado__

.. moduleauthor:: Roberto Benéitez Vaquero
"""
#TODO: listar los Formularios que hay aquí para Sphinx, en multilinea.


from django import forms
from django.core import validators
from forecasting.models import Inmueble


class InmuebleForm(forms.ModelForm):
    """
    Formulario para la creación de un Inmueble.
    """

    # TODO: No funciona ninguno de estos validadores. Lo mismo sí funcionan, pero no esoty usando la información limpiada para rellenar mi modelo, a pesar de que se limpien los datos
    nombre = forms.CharField(validators=[validators.validate_unicode_slug,
                                         validators.validate_slug,
                                         validators.MinLengthValidator(3),
                                         validators.MaxLengthValidator(5)])
    descripcion = forms.CharField(validators=[validators.validate_unicode_slug,
                                              validators.MaxLengthValidator(255)])
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Inmueble
        fields=('nombre', 'descripcion')

    def __init__(self, *args, **kwargs):
        user=kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

