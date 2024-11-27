# final_pjt 'MVBeer'

📚 프로젝트 정리
#### 프로젝트 개요

- 프로젝트 이름: 🎥 MVBeer 

    movie와 beer의 합성어로, 술과 영화를 함께 즐기는 사람들이라는 의미로 이름을 지었습니다. 

- 설명:

    사용자들에게 인기 영화, 영화별 주류 및 주류별 영화 추천, 검색 기능을 제공하며, Vue.js 프론트엔드와 Django 백엔드로 구현된 영화 정보를 기반으로 한 웹 애플리케이션입니다.
    

#### 주요 기술 스택

- 프론트엔드: Vue 3, Pinia (State Management), Vue Router, Axios
- 백엔드: Django, Django REST Framework (DRF)
- API 통신: REST API (DRF로 제공된 데이터와 Vue에서 Axios를 활용한 API 연동)
- 기타: Git (버전 관리)


프로젝트 주요 기능
1. 영화 목록 조회
    
    - 구현 내용: 
    
        백엔드에서 영화 데이터를 JSON 형태로 제공.
        프론트엔드에서 getMovies API 호출 후 상태 관리를 통해 전체 영화 목록 표시.
    
    - 구현 원리:
        movies 상태를 Pinia의 store에서 관리.
        Axios를 사용해 Django REST API로부터 데이터를 가져와 상태 업데이트.
        결과: 모든 영화가 리스트 형태로 화면에 표시되며, 슬라이싱 또는 필터링 가능.

2. 영화 상세 정보 조회
    
    - 구현 내용:
        
        각 영화의 ID(movie_id)로 특정 영화의 상세 정보를 불러와 출력.
        프론트엔드 라우트 동적 매핑: movies/:movie_id/ 형태로 구성.
    
    - 구현 원리:
        
        URL 매개변수를 Vue Router에서 사용하여, 특정 영화의 movie_id를 경로에 전달.
        Axios로 백엔드 API 호출하여 상세 데이터를 가져온 뒤 화면에 출력.
        결과: 사용자가 클릭한 영화의 자세한 정보를 별도의 상세 페이지에서 확인 가능.

3. 장르별 영화 추천
    - 구현 내용:
        특정 장르에 속한 영화를 필터링해 추천.
        각 장르는 genres 테이블에서 관계형 필드를 통해 관리.
    - 구현 원리:
        Django Many-to-Many 관계로 영화와 장르를 매핑.
        Vue에서 filter 메서드를 사용하여 특정 장르의 ID를 기준으로 필터링된 영화 표시.
    - 결과: 사용자가 특정 장르를 선택하면 관련 영화만 출력.

4. 검색 기능
    - 구현 내용:
        사용자가 입력한 키워드에 따라 영화 제목이나 줄거리에서 일치하는 영화 표시.
    - 구현 원리:
        Django REST API에서 GET 요청 시 q 매개변수로 키워드 전달.
        DRF에서 해당 키워드에 해당하는 영화 쿼리셋 반환.
        Vue에서 검색 결과를 받아 상태를 업데이트하고 화면에 표시.   
    - 결과: 실시간 검색이 가능하며, 정확한 키워드 매칭 또는 부분 매칭 가능.
5. 캐러셀 컴포넌트
    - 구현 내용:
        영화 데이터를 원형으로 배치하여 캐러셀 형태로 표시.
        슬라이드 이동 시 영화가 회전하며 보여짐.
    - 구현 원리:
        CSS transform: rotateY와 translateZ를 사용한 3D 캐러셀 구현.
        Vue의 computed와 상태 관리로 영화 데이터를 순회하며 스타일 업데이트.
    - 결과: 사용자 친화적인 UI로 영화 목록을 스크롤 없이 쉽게 탐색 가능.
6. 데이터 모델링 및 API 설계
    - 구현 내용:
        Django의 ORM과 DRF를 활용해 영화, 장르, 사용자 댓글 등을 모델링.
    - 구현 원리:
        Movie 모델: movie_id, title, summary, genres, release_date 등의 필드 정의.
        Genre 모델: 영화와 다대다 관계를 가지며 name 필드 포함.
        Comment 모델: 특정 영화에 댓글을 작성할 수 있도록 사용자와 영화 간의 외래 키 관계 정의.
    - 결과: 명확한 데이터 관계와 효율적인 API 제공.

주요 코드 요약

1. Django 모델
```py
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200) 
    summary = models.TextField()
    release_date = models.DateField() 
    director = models.CharField(max_length=100) 
    genres = models.ManyToManyField(
        MovieGenre, 
        related_name="movies"
    )  # 장르 (N:1 관계)
    star_rating = models.DecimalField(max_digits=3, decimal_places=1) 
    poster_url = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.title

class MovieGenre(models.Model):
    name = models.CharField(max_length=100)  # 영화 장르명
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)  # 큰 범주 연결
    subtype = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name
```

2. Vue.js Store (Pinia)
```js
export const useMovieStore = defineStore('movie', () => {
  const movies = ref([ ]) // 전체영화목록 
  const movie_detail = ref(null) // 단일 영화 상세
  const genres = ref([])
  const API_URL = 'http://127.0.0.1:8000'

   // 전체 영화 목록
  const getMovies = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
    .then((res) => {
      movies.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  // 영화 상세
  const getMovie = function(moviePk) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/${moviePk}`
    })
    .then((res) => {
      movie_detail.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  // 영화 장르
  const getGenres = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/genres/` 
    })
    .then((res) => {
      genres.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
  };

  return { movies, getMovies, getMovie, movie_detail, getGenres };
})
```

3. Vue 컴포넌트
```vue
<template>
  <div class="carousel-container">
    <div class="carousel">
      <div
        v-for="movie in filteredMovies"
        :key="movie.id"
        class="carousel-item"
      >
        <MovieMainInfo :movie="movie" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useMovieStore } from "@/stores/movie";

const store = useMovieStore();
const filteredMovies = computed(() => {
  return store.movies.filter(movie => [912649, 1100782, 1184918].includes(movie.id));
});
</script>
```


#### 배운 점 및 개선 사항

- REST API의 설계 및 활용:

    효율적인 데이터 제공과 명확한 엔드포인트 구조의 중요성을 배움.
    URL 파라미터 및 쿼리스트링 사용의 유용성을 확인.

- Vue 상태 관리 (Pinia):

    중앙 집중화된 상태 관리로 코드의 가독성과 유지보수성을 높임.

- 3D UI/UX 구현:

    CSS3와 Vue를 활용해 사용자가 직관적으로 접근할 수 있는 UI를 구현.

- 향후 개선 사항:

    




## 20241118
* ERD 설계

## 20241119


## 20241120
* Vue Router를 활용한 SPA 라우팅 구현

## 20241121

* Git clone 새로 받거나 pull 받아온 뒤에 해야할 일!

    내가 작업하던 브랜치(ej, sm)으로 옮겨가기

* Back(Django)

    1. .env에 API_KEY 적어놓기

    2. 가상환경(venv) 설치

        `python -m venv venv`

        Window: `source venv/Scripts/activate`
        
        Mac: `source venv/bin/activate`

    3. `pip install -r requirements.txt`
    
        (전역에 `django-cors-headers`, `pillow` 설치 안되어 있으면 실행 안되는게 있을 수도 있다. 전역에도 설치하고 가상환경에도 install 하자!)

        `pip install django-cors-headers`
        
        `pip install pillow`    
            
        `pip install djangorestframework`
        

    4. `python manage.py makemigrations`

    5. `python manage.py migrate`

    6. 데이터 load 하기

        `python manage.py loaddata beverage.json`

        `python manage.py loaddata movie_genre.json`

        `python manage.py loaddata beverage_detail.json movie_data.json`

    7. alcohol.py 실행해서 media에 있는 image 업로드 하기

        **각 주류 파일에 있는 이미지명(blanc.jpg...), beverage_detail의 examples에 적힌 주류명이 완전히 일치**해야 이미지가 업로드 된다.

    8. 서버 실행 
        `python manage.py runserver`

* front(vue3)
    1. vue project로 이동

        `cd front/mov_eer`

    2. 설치할 것들 

        `npm i`

        `npm install axios`

        - pinia plugin 어쩌구 설치 및 등록하기  
            `npm i pinia-plugin-persistedstate`

            ```js
            import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

            const pinia = createPinia()

            pinia.use(piniaPluginPersistedstate)

            app.use(pinia)

            // stores/counter.js(스토어) 예시
            export const useCounterStore = defineStore('counter', () => {
                return {}
            }, {persist: true})

            ```
        설치, 등록 하면 브라우저의 local storage에 저장된다.(개발자도구-> Application -> local storage에서 확인)

    3. 서버 실행

        `npm run dev`


## 20241122
* back 로그인 기능 구현
  
  `pip install dj-rest-auth`

  `pip install 'dj-rest-auth[with-social]'`

## 20241123
* 로고 디자인 완료
* comment 생성 기능 구현
* 주류 상세 페이지 초기 설계 및 API 연결

## 20241124
* comment 수정, 삭제 안되는 부분 수정 완료
* 주류 상세페이지 작성
* 검색 기능 Vue 컴포넌트 설계

## 20241125
* 검색 기능 구현 완료
* css 수정

## 20241126

* 메인페이지에 올릴 영화 필터링
* 주류별 영화 추천에 영화 넘기는 기능