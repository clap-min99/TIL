### Project04
#### Content
- 영화 커뮤니티 웹 서비스 화면 및 데이터 구성
- 영화 데이터 생성, 조회, 수정, 삭제가 가능한 어플리케이션 완성

#### 목표
- Django model과 orm에 대한 이해 
- Django form에 대한 이해 
- Django static files 관리에 대한 이해 -> 9/26 복습
- bootstrap component 및 grid system을 활용한 반응형 레이아웃 구성 



##### VIEWS

- 기본 페이지
    ```py
    def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)
    ```

    - Movie.objects.all()
        : model 전체 불러오기


#### MODELS
```py
from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True)
    
```

투비 컨티뉴