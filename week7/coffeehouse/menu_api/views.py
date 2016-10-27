from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

from menu_api.models import Special, Ingredient
from menu_api.serializers import SpecialSerializer, IngredientSerializer


class SpecialListCreateAPIView(ListCreateAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer


class SpecialUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer


class IngredientListAPIView(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetailAPIView(RetrievedAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
