from rest_framework import serializers
from . models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['movie', 'review', 'rating', 'id']

    def create(self, validated_data):
        return Review.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.movie = validated_data.get('movie', instance.movie)
        instance.review = validated_data.get('review', instance.review)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True, source='review_set')
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'id', 'reviews']

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.year = validated_data.get('year', instance.year)
        instance.director = validated_data.get('director', instance.director)
        instance.save()
        return instance

