from ..models import Usuario


def get_usuario(i):
    usuario = Usuario.objects.all().get(id=i)
    return usuario


def get_productos_comprados_usuario(i):
    usuario = get_usuario(i)
    productos_comprados_usuario = usuario.productos_comprados.all()
    return productos_comprados_usuario


def get_productos_recomendados_usuario(i):
    usuario = get_usuario(i)
    productos_recomendados_usuario = usuario.productos_recomendados.all()
    return productos_recomendados_usuario


def create_usuario(form, correo):
    usuario = form.save()
    usuario.correo = correo
    usuario.save()
    return ()

def get_usuario_correo(correo):
    usuario = Usuario.objects.all().get(correo=correo)
    return usuario
