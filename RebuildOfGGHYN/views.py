from django.views.generic import TemplateView

from datetime import datetime, timedelta
from typing import Dict, Any


# sin uso actual, antes era el html de bienvenida
class TestPage(TemplateView):
    template_name = 'test.html'

# sin uso actual, antes era el html de desdepedida
class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class BienvenidaPage(TemplateView):
    template_name = 'bienvenida_usuario.html'


class DespedidaPage(TemplateView):
    template_name = 'despedida_usuario.html'

class AterrizajePage(TemplateView):
    template_name = 'accounts/aterrizaje.html'


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        now = datetime.now().__format__('%Y-%m-%d')
        context = super().get_context_data(**kwargs)
        context['index_fecha'] = now
        return context
