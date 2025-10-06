from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from configapp.serializers import *
from rest_framework.viewsets import ModelViewSet


class LanguageView(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PageView(APIView):
    def get(self, request, lang_id=None):
        if lang_id:
            language = get_object_or_404(PageModels, lang=lang_id)
        else:
            language = get_object_or_404(PageModels, lang__title='uz')
        serializer = PageSerializer(language)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=PageSerializer)
    def post(self, request):
        serializer = PageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    @swagger_auto_schema(request_body=PageSerializer)
    def put(self, request, lang_id):
        page = get_object_or_404(PageModels, lang=lang_id)
        serializer = PageSerializer(page, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=PageSerializer)
    def patch(self, request, lang_id):
        page = get_object_or_404(PageModels, lang=lang_id)
        serializer = PageSerializer(page, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, lang_id):
        page = get_object_or_404(PageModels, lang=lang_id)
        page.delete()
        return Response(
            {"detail": "Ma'lumot muvaffaqiyatli o'chirildi."},
            status=status.HTTP_204_NO_CONTENT
        )


class ContentView(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentTextView(ModelViewSet):
    queryset = ContentText.objects.all()
    serializer_class = ContentTextSerializer

class ContentFileView(ModelViewSet):
    queryset = ContentFile.objects.all()
    serializer_class = ContentFileSerializer

class ContentImageView(ModelViewSet):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer

class ContentVideoView(ModelViewSet):
    queryset = ContentVideo.objects.all()
    serializer_class = ContentVideoSerializer