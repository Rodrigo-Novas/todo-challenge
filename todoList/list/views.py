import re
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from list.models import Lista
from list.serializers import ListaSerializer
import logging
from datetime import date, datetime



logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def list_todo(request) -> Response:
    """
    List all todos.
    :return: Retorna la respuesta con codigo 200 si obtuvo la lista, 201 si se creo y 400 si no se pudo ejecutar
    :treturn: Response
    """
    if request.method == 'GET':
        logger.info('Obtaining Todo!')
        lista = Lista.objects.all()
        serializer = ListaSerializer(lista, many=True)
        logger.info('Lista obtaining!')
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        description = request.data.get("description")
        status_code = False
        creation_date = datetime.today().strftime('%Y-%m-%d')
        serializer = ListaSerializer(
            data={"description": description, "status": status_code, "creation_date": creation_date})
        logger.info('Insert Lista!')
        if serializer.is_valid():
            serializer.save()
            logger.info('Lista inserted!')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.info('Not inserted!')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def lista_delete(request, lista_id: int) -> Response:
    """
    DELETE Lista.
    :return: Retorna la respuesta con codigo 200 si obtuvo la lista y 404 si no se pudo encontrar
    :treturn: Response
    """
    lista = Lista.objects.filter(id=lista_id).first()
    logger.info(f'Obtaining id {lista_id}!')
    if not lista is None:
        Lista.objects.get(id=lista_id).delete()
        logger.info(f'Delete lista with id {lista_id}!')
        return Response(f"El id {lista_id} fue eliminado con exito", status=status.HTTP_200_OK)
    else:
        logger.info('Lista not deleted')
        return Response(f"El id {lista_id} no pudo ser encontrado", status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_lista(request, lista_id: int) -> Response:
    """
    UPDATE lista.
    :return: Retorna la respuesta con codigo 200 si obtuvo la lista, 201 si se creo, 400 si no lo puede ejecutar y 404 si no se pudo encontrar
    :treturn: Response
    """
    lista = Lista.objects.filter(id=lista_id).first()
    if not lista is None:
        serializer = ListaSerializer(lista, data=request.data, partial=True)
        logger.info('Updating lista!')
        if serializer.is_valid():
            serializer.save()
            logger.info('Lista updated')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        logger.info('Lista not deleted')
        return Response(f"El id {lista_id} no pudo ser encontrado", status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def status_completed(request, lista_id: int) -> Response:
    """
    UPDATE status.
    :return: Retorna la respuesta con codigo 200 si obtuvo la lista, 201 si se creo y 404 si no se pudo encontrar
    :treturn: Response
    """
    lista = Lista.objects.filter(id=lista_id).first()
    if not lista is None:
        status_code = True
        serializer = ListaSerializer(
            lista, data={"status": status_code}, partial=True)
        logger.info('Updating lista!')
        if serializer.is_valid():
            serializer.save()
            logger.info('Lista updated')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        logger.info('Lista not deleted')
        return Response(f"El id {lista_id} no pudo ser encontrado", status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def filter_lista_by(request, date: str, description: str = None) -> Response:
    """
    filter Lista.
    :return: Retorna la respuesta con codigo 302 si se encontro y 404 si no se pudo ejecutar
    :treturn: Response
    """
    if not description is None:
        logger.info('Obtaining lista with date and description!')
        lista = Lista.objects.filter(
            creation_date=date, description=description).all()
        if lista.exists():
            serializer = ListaSerializer(lista, many=True)
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        else:
            return Response("No se encontraron datos", status=status.HTTP_404_NOT_FOUND)
    else:
        logger.info('Obtaining lista with only date')
        lista = Lista.objects.filter(creation_date=date).all()
        if lista.exists():
            serializer = ListaSerializer(lista, many=True)
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        else:
            logger.info('Not found data!')
            return Response("No se encontraron datos", status=status.HTTP_404_NOT_FOUND)
