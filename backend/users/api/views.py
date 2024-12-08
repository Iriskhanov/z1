from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework_simplejwt.authentication import JWTAuthentication
from property.models import Property
from users.api.serializers import UserRegistrationSerializer



class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Регистрация успешна!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProtectedResourceView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Добро пожаловать, {request.user.username}! Это защищенный ресурс."})
    
class ToggleFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, property_id):
        # Получаем объект недвижимости
        property_obj = get_object_or_404(Property, id=property_id)
        
        # Добавляем или удаляем объект из избранного
        if property_obj in request.user.favorites.all():
            request.user.favorites.remove(property_obj)
            action = "removed"
        else:
            request.user.favorites.add(property_obj)
            action = "added"

        return Response({"status": "success", "action": action}, status=HTTP_200_OK)