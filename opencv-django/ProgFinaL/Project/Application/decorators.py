from django.shortcuts import redirect,get_object_or_404
from urllib.parse import urlencode
from user.models import User

def tiene_modelo(funcion_vista):
    def wrapper(request, *args, **kwargs):
        user_id = request.user.id
        usuario = get_object_or_404(User, id=user_id)
        if usuario.model == True:
            return funcion_vista(request, *args, **kwargs)
        else:
            mensaje = "Parece que estas emocionad@. Para poder subir tus fotos, necesitamos de algunos datos adicionales."
            params = urlencode({'mensaje': mensaje})
            return redirect(f'/homeInicio/{user_id}/?{params}')
    return wrapper

