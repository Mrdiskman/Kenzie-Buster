from .models import AgeRestriction
from rest_framework import serializers
from .models import Movie, MovieOrder

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating =  serializers.ChoiceField(choices=AgeRestriction.choices, default=AgeRestriction.G)
    synopsis = serializers.CharField(default=None, allow_null=True)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, object:Movie):
        return object.user.email

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)
#-------------------------------------------------------------------------------#
class MovieOrderSerializer(serializers.Serializer):
      id = serializers.IntegerField(read_only=True)
      title = serializers.SerializerMethodField()
      buyed_at = serializers.DateTimeField(read_only=True)
      price = serializers.DecimalField(max_digits=8, decimal_places=2)
      buyed_by = serializers.SerializerMethodField()

      def get_buyed_by(self, object: MovieOrder):
         return object.user.email

      def get_title(self, object: MovieOrder):
         return object.movie.title

      def create(self, validated_data:dict) -> MovieOrder:
         buy= MovieOrder.objects.create(**validated_data)
         return buy