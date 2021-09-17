from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Keyboards
from .serializers import KeyboardSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_keyboards(request):
    keyboards = Keyboards.objects.all()
    serializer = KeyboardSerializer(keyboards, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_keyboards(request):
    if request.method == 'POST':
        serializer = KeyboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(keyboard=request.keyboard)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        keyboards = Keyboards.objects.filter(user_id=request.user.id)
        serializer = KeyboardSerializer(keyboards, many=True)
        return Response(serializer.data)

