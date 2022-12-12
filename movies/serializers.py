from .models import AgeRestriction
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating =  serializers.ChoiceField(allow_null=True, choices=AgeRestriction.choices)
    synopsis = serializers.CharField(default=None, allow_null=True)
    added_by = serializers.CharField(read_only=True)

    def create(self, validated_data: dict):
       
        return Movie.objects.create(**validated_data)