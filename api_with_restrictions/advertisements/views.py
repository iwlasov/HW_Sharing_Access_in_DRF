from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters
#from rest_framework.response import Response
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer

from django_filters.rest_framework import DjangoFilterBackend

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
       
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['creator', 'status']
    filterset_class = AdvertisementFilter

    def get_permissions(self):

        """Получение прав для действий."""
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        return []

        #"""Получение прав для действий."""
        #if self.action in ["create", "update", "partial_update"]:
        #    return [IsAuthenticated()]
        #return []
