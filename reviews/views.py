from rest_framework import viewsets, filters, generics
from reviews.models import Critico
from reviews.serializers import CriticoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CriticoViewSet(viewsets.ModelViewSet):
    queryset = Critico.objects.all().order_by('nome')
    serializer_class = CriticoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    http_method_names = ['get', 'post', 'put', 'patch']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # def create(self, request):
    #     """Cabeçalho Location"""
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         response = Response(serializer.data, status=status.HTTP_201_CREATED)
    #         id = str(serializer.data['id'])
    #         response['Location'] = request.build_absolute_uri() + id
    #         return response
