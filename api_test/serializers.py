from rest_framework import serializers


class TranslateApiSerializer(serializers.Serializer):
    name = serializers.CharField(help_text='Напишите название фильма на английском - получите перевод и данные.')