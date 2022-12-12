from rest_framework.views import APIView, Request, Response, status
from .serializers import MovieSerializer
from .models import Movie
from .permissions import MyCustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication 

class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self, request:Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, 201)

    def get(self, request: Request) -> Response:
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)

        return Response(serializer.data)
