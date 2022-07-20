from django import forms
from . import models

# Formulario para la creación de un nuevo Inmueble
class InmuebleForm(forms.ModelForm):
    """
    Formulario para la creación de un Inmueble.
    """

    class Meta():
        model = models.Inmueble
        fields=('nombre', 'descripcion')

    def __init__(self, *args, **kwargs):
        user=kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

