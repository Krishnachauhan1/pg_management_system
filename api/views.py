from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import *
from .serializer import *


class PgsViewSet(viewsets.ModelViewSet):
    queryset = Pgs.objects.all()
    serializer_class = PgsSerializer

class UsersViewSet(viewsets.ModelViewSet):

    queryset = Users.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], url_path='login')  # /users/login/
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # For now, plain text password check (use hashed passwords in production)
        if user.password != password:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "pg_id": user.pg.id,
            
            }
        }) 
    
class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer   