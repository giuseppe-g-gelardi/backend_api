from rest_framework import serializers
from .models import User
from .models import Keyboards

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboards
        fields = ['id', 'layout', 'angle', 'body_material', 'body_finish_alu', 'body_finish_pc', 'plate_material', 'plate_finish_alu', 'plate_finish_brass', 'plate_finish_pc', 'weight_material', 'weight_finish_all', 'mounting_style']

