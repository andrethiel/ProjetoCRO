import os
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import controller


@api_view(['POST'])
def Arquivo(request):

    numero = request.data['numero']
    arquivo = request.FILES.get('arquivo')

    destination = open("./quickstart/media/" + arquivo.name, 'wb+')

    if(arquivo.content_type == 'application/pdf'):

        for item in arquivo.chunks():
            destination.write(item)
        destination.close()
        response = controller.verificaArquivo(
            arquivo=arquivo.name, numero=numero)
        if(response == True):
            os.remove("./quickstart/media/" +
                      arquivo.name.replace(".pdf", ".jpeg"))
            return Response(response)

    return Response("aaaa")
