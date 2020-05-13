from ..models import Componente


def get_all_componentes():
    componentes = Componente.objects.all()
    return componentes

def get_component(id):
    componente = Componente.objects.all().filter(id=id)
    return componente
