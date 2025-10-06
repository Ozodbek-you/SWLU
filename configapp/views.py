from django.shortcuts import render
from configapp.serializers import *
from rest_framework.viewsets import ModelViewSet


class LanguageView(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


