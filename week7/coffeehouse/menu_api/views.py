from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from menu_api.models import Special
from menu_api.serializers import SpecialSerializer


class SpecialListAPIView(ListCreateAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer


class SpecialDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
