from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validation_data):
        return Movie.objects.create(**validation_data)
    
    def update(self, instance, validation_data):
        instance.name = validation_data.get('name', instance.name)
        instance.description = validation_data.get('description', instance.description)
        instance.active = validation_data.get('active', instance.active)
        instance.save()
        return instance