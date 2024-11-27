from django.db import models
from django.conf import settings

# 알콜 모델들

class Beverage(models.Model):
    type = models.CharField(max_length=50)  # 주류 유형 (Beer, Whiskey 등)

    def __str__(self):
        return self.type


class Beer(models.Model):
    beverages = models.ManyToManyField(Beverage, related_name='beers')
    subtype = models.CharField(max_length=50)  # 에일, 라거 등
    description = models.TextField(blank=True, null=True)
    examples = models.TextField()

    def __str__(self):
        return self.subtype


class BeerImage(models.Model):
    beer = models.ForeignKey(Beer, related_name='images', on_delete=models.CASCADE)  # 다대일 관계
    image = models.ImageField(upload_to='beer_images/')  # 이미지 저장 필드
    description = models.CharField(max_length=255, blank=True, null=True)  # 이미지 설명 (선택)

    def __str__(self):
        return f"Image for {self.beer.subtype}"


class Whiskey(models.Model):
    beverages = models.ManyToManyField(Beverage, related_name='whiskies')
    subtype = models.CharField(max_length=50)  # 버번, 스카치 등
    description = models.TextField(blank=True, null=True)
    examples = models.TextField()

    def __str__(self):
        return self.subtype


class WhiskeyImage(models.Model):
    whiskey = models.ForeignKey(Whiskey, related_name='images', on_delete=models.CASCADE)  # 다대일 관계
    image = models.ImageField(upload_to='whiskey_images/')  # 이미지 저장 필드
    description = models.CharField(max_length=255, blank=True, null=True)  # 이미지 설명 (선택)

    def __str__(self):
        return f"Image for {self.whiskey.subtype}"


class Wine(models.Model):
    beverages = models.ManyToManyField(Beverage, related_name='wines')
    subtype = models.CharField(max_length=50)  # 레드, 화이트 등
    description = models.TextField(blank=True, null=True)
    examples = models.TextField()

    def __str__(self):
        return self.subtype


class WineImage(models.Model):
    wine = models.ForeignKey(Wine, related_name='images', on_delete=models.CASCADE)  # 다대일 관계
    image = models.ImageField(upload_to='wine_images/')  # 이미지 저장 필드
    description = models.CharField(max_length=255, blank=True, null=True)  # 이미지 설명 (선택)

    def __str__(self):
        return f"Image for {self.wine.subtype}"


class NonAlcohol(models.Model):
    beverages = models.ManyToManyField(Beverage, related_name='nonalcohols')
    subtype = models.CharField(max_length=50)  # 콜라, 사이다 등
    description = models.TextField(blank=True, null=True)
    examples = models.TextField()

    def __str__(self):
        return self.subtype


class NonAlcoholImage(models.Model):
    nonalcohol = models.ForeignKey(NonAlcohol, related_name='images', on_delete=models.CASCADE)  # 다대일 관계
    image = models.ImageField(upload_to='nonalcohol_images/')  # 이미지 저장 필드
    description = models.CharField(max_length=255, blank=True, null=True)  # 이미지 설명 (선택)

    def __str__(self):
        return f"Image for {self.nonalcohol.subtype}"


# 영화 모델들

class MovieGenre(models.Model):
    name = models.CharField(max_length=100)  # 영화 장르 이름
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)  # 큰 범주 연결
    subtype = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)  # 영화 제목
    summary = models.TextField()  # 줄거리
    release_date = models.DateField()  # 개봉일
    director = models.CharField(max_length=100)  # 감독 이름
    actors = models.CharField(max_length=100)  # 주연 배우 이름
    genres = models.ManyToManyField(
        MovieGenre, 
        related_name="movies"
    )  # 장르 (N:1 관계)
    adult = models.BooleanField()  # 성인 or not
    star_rating = models.DecimalField(max_digits=3, decimal_places=1)  # 별점 (예: 4.5)
    poster_url = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


