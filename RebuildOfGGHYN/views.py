from django.views.generic import TemplateView

from datetime import datetime, timedelta
from typing import Dict, Any


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class BienvenidaPage(TemplateView):
    template_name = 'bienvenida_usuario.html'


class DespedidaPage(TemplateView):
    template_name = 'despedida_usuario.html'


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        now = datetime.now().__format__('%Y-%m-%d')
        context = super().get_context_data(**kwargs)
        context['index_fecha'] = now
        return context
