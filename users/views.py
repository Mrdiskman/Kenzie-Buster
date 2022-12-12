from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView


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
