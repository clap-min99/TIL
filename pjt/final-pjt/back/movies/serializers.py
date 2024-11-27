from rest_framework import serializers
from .models import Movie, MovieGenre, Beverage, Whiskey, Beer, Wine, NonAlcohol, BeerImage, WineImage, WhiskeyImage, NonAlcoholImage, Comment

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title', 'summary', 'poster_url', 'genres', 'release_date', 'star_rating', 'poster_url')


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_genres(self, obj):
        return [
            {
                "id": genre.id,
                "name": genre.name,
                "recommended_beverage": {
                    "type": genre.beverage.type,  # 큰 범주
                    "subtype": genre.subtype  # 세부 주류
                }
            }
            for genre in obj.genres.all()
        ]

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = ['id', 'name', 'beverage', 'subtype']



class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = '__all__'

class BeerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerImage
        fields = ['image', 'description']

class BeerSerializer(serializers.ModelSerializer):
    images = BeerImageSerializer(many=True, read_only=True)

    class Meta:
        model = Beer
        fields = ['id', 'subtype', 'description', 'examples', 'images']


class WhiskeyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiskeyImage
        fields = ['image', 'description']

class WhiskeySerializer(serializers.ModelSerializer):
    images = WhiskeyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Whiskey
        fields = ['id', 'subtype', 'description', 'examples', 'images']


class WineImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WineImage
        fields = ['image', 'description']

class WineSerializer(serializers.ModelSerializer):
    images = WineImageSerializer(many=True, read_only=True)

    class Meta:
        model = Wine
        fields = ['id', 'subtype', 'description', 'examples', 'images']


class NonAlcoholImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonAlcoholImage
        fields = ['image', 'description']

class NonAlcoholSerializer(serializers.ModelSerializer):
    images = NonAlcoholImageSerializer(many=True, read_only=True)

    class Meta:
        model = NonAlcohol
        fields = ['id', 'subtype', 'description', 'examples', 'images']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)  # user를 username으로 반환
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']
        read_only_fields = ('user', 'movie')

        
