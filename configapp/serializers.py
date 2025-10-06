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


