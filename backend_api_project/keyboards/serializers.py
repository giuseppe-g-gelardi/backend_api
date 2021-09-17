from rest_framework import serializers
from .models import Keyboards

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboards
        fields = ['id', 'layout', 'color', 'keycap_color']

