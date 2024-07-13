from django.shortcuts import render,get_object_or_404
from reconocimientoFacial.recolectar_datos import generar_imagenes
from reconocimientoFacial.entrenamiento_redneural import crearModeloDNN
from reconocimientoFacial.buscandoSimilitudes import buscando
from django.http import HttpResponse, HttpResponseServerError,StreamingHttpResponse
from user.models import User




def recolectarDatos(request):
    return StreamingHttpResponse(generar_imagenes(request), content_type='multipart/x-mixed-replace; boundary=frame')



def reconocimientoFacial(request):
    return render(request, 'reconocimientoFaciial/reconocimientoFacial.html')




import logging
# Configura el logger
logger = logging.getLogger(__name__)

def entrenarModelo(request, user_id):
    nombreUsuario = request.user.username  
    try:
        crearModeloDNN(nombreUsuario , user_id)
        
        response = """
        <script>
            alert("Modelo entrenado exitosamente.");
            window.location.href = "/album";
        </script>
        """
        return HttpResponse(response)
    except Exception as e:
        logger.error(f'Error al entrenar el modelo para el usuario {nombreUsuario}: {e}')
        response = """
        <script>
            alert("Hubo un error al entrenar el modelo. Por favor, inténtelo de nuevo más tarde.");
            window.location.href = "/album";
        </script>
        """
        return HttpResponseServerError(response)

    
def buscandoSimilitudes(request):
    nombreUsuario = request.user
    return buscando(nombreUsuario)
# def buscandoSimilitudes(request):
#     nombreUsuario = request.user
#     try:
#         buscando(nombreUsuario)
#         response ="""
#         <script>
#             window.location = "/album";
#             alert("Modelo entrenado exitosamente.");
            
#         </script>
#         """
#         return HttpResponse(response)
#     except Exception as e:
#         return HttpResponseServerError({'error': str(e)})
    