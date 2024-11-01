from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):

    class ActorMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    movie = ActorMovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class MovieDetailSerializer(serializers.ModelSerializer):
    class ReviewMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content',)
    
    review_set = ReviewMovieSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    movie = MovieReviewSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'