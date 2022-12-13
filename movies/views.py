from rest_framework.views import APIView, Request, Response, status
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication 
from .permissions import MyCustomPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self, request:Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user = request.user)

        return Response(serializer.data, 201)

    def get(self, request: Request) -> Response:
        movie = Movie.objects.all()
        result_page = self.paginate_queryset(movie, request)
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

class MovieDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]
    
    def get(self, request: Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieOrders(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie = movie, user = request.user )
        
        return Response(serializer.data, 201)
