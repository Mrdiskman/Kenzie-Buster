from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication 
from .permissions import UserCustomPermission
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def get(self, request: Request) -> Response:
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, 201)
        
class LoginView(TokenObtainPairView):
    ...

class UserDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserCustomPermission]

    def get(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
