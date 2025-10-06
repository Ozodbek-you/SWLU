from rest_framework import serializers

from configapp.models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageModels
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class ContentTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentText
        fields = '__all__'

class ContentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentFile
        fields = '__all__'

class ContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImage
        fields = '__all__'

class ContentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentVideo
        fields = '__all__'