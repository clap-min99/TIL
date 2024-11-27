<template>
  <div class="ale-view">
    <h1>🍺 에일(Ale)</h1>
    <div class="ale-intro">
      <img
        src="@/assets/IPA.png"
        alt="Ale Beer"
        class="ale-image"
      />
      <div class="ale-description">
        <p>
          <strong>에일(Ale)</strong>은 상면 발효 방식으로 만들어지는 맥주로, 발효 온도가 높아
          과일향과 풍부한 풍미를 느낄 수 있는 것이 특징입니다.
          에일은 역사적으로 가장 오래된 맥주 스타일 중 하나로,
          IPA, 페일 에일, 포터, 벨지안 에일 등 다양한 종류를 가지고 있습니다.
          특히, 독특한 향과 맛 덕분에 전 세계에서 사랑받고 있습니다.
        </p>
        <p> 현대에 와서는 전 세계적으로 라거가 점유율에서 우위를 차지하고 있지만, 영국과 벨기에 같은 국가에서는 여전히 에일이 대중적인 주종으로 자리 잡고 있습니다. 
          특히 영국에서는 맥주를 의미하는 단어로 "Beer" 대신 "Ale"이라는 표현이 사용될 정도로 에일이 친숙합니다. 
          <strong>중세 시대를 배경으로 한 영화나 만화에서 나무잔에 담긴 맥주를 벌컥벌컥 마시는 장면은 대부분 에일을 묘사</strong>한 것입니다.</p>
        <p class="ale-action-pairing">
          🍿 에일은 액션 영화와 환상적인 조합을 이룹니다.
          입안 가득 퍼지는 에일의 과일향과 톡 쏘는 홉의 쓴맛은 영화 속 화려한 액션 장면의 짜릿함을 더해줍니다.
          시원한 한 모금과 함께 스펙터클한 순간들을 즐겨보세요!
        </p>
      </div>
    </div>

    <div class="beer-list">
      <h2></h2>
      <div class="beer-card-container">
        <div v-for="beer in beers" :key="beer.id" class="beer-card">
          <h3>{{ beer.name }}</h3>
          <p>{{ beer.description }}</p>
          <p><strong>대표 브랜드:</strong> {{ beer.representativeBrands }}</p>
          <p><strong>스타일:</strong> {{ beer.style }}</p>
          <p>
            <strong>추천 안주:</strong> {{ beer.foodPairing }}
            <span>{{ beer.foodEmoji }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="movies-scroll">
    <h2>페어링 with 에일🍺</h2>
    <div class="movie-card-container">
      <div
        v-for="movie in paginatedMovies"
        :key="movie.id"
        class="movie-card"
      >
        <RouterLink :to="{ name: 'MovieDetailView', params: { moviePk: movie.id } }">
          <img :src="getImageUrl(movie.poster_url)" class="movie-poster" alt="Movie Poster" />
        </RouterLink>
        <p class="movie-title">{{ movie.title }}</p>
      </div>
    </div>

    <!-- 페이지 네비게이션 -->
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">이전</button>
        <span> {{ currentPage }} / {{ totalPages }}</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useLiquorStore } from "@/stores/liquor";
import { useMovieStore } from "@/stores/movie";
import { onMounted } from "vue";
import { RouterLink } from "vue-router";
import { ref, computed } from "vue";

const currentPage = ref(1);
const itemsPerPage = 30; // 한 페이지에 표시할 영화 개수

// 페이징된 영화 목록
const paginatedMovies = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return getBeerMovies('Ale').slice(start, end);
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getBeerMovies('Ale').length / itemsPerPage);
});

// 페이지 네비게이션 함수
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value -= 1;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value += 1;
  }
};

const beers = [
  {
    id: 1,
    name: "IPA (India Pale Ale)",
    description: "홉의 풍미가 강렬하고 과일 향이 나는 에일.",
    representativeBrands: "BrewDog Punk IPA, Sierra Nevada IPA",
    style: "IPA",
    foodPairing: "매운 음식, 치즈 플래터",
    foodEmoji: "🌶️🧀"
  },
  {
    id: 2,
    name: "페일 에일 (Pale Ale)",
    description: "홉과 몰트의 조화로운 맛과 밝은 색깔이 특징인 에일.",
    representativeBrands: "Sierra Nevada Pale Ale, London Pride",
    style: "페일 에일",
    foodPairing: "구운 고기, 피자",
    foodEmoji: "🍖🍕"
  },
  {
    id: 3,
    name: "포터 (Porter)",
    description: "부드럽고 초콜릿 풍미가 느껴지는 흑맥주.",
    representativeBrands: "Fuller’s London Porter, Baltika Porter",
    style: "포터",
    foodPairing: "스테이크, 초콜릿 디저트",
    foodEmoji: "🥩🍫"
  },
  {
    id: 4,
    name: "벨지안 에일 (Belgian Ale)",
    description: "풍부한 향신료와 과일 향이 독특한 벨기에 스타일의 에일.",
    representativeBrands: "Duvel, Leffe Blond",
    style: "벨지안 에일",
    foodPairing: "치즈 플래터, 조개 요리",
    foodEmoji: "🧀🦪"
  }
];

const liquorStore = useLiquorStore();
const movieStore = useMovieStore();

onMounted(() => {
  liquorStore.getBeers();
  movieStore.getMovies();
  movieStore.getGenres();
});

const getBeerMovies = (subtype) => {
  return movieStore.movies.filter((movie) => {
    return movie.genres.some((genreId) => {
      const genre = movieStore.genres.find((g) => g.id === genreId);
      return genre && genre.subtype === subtype;
    });
  });
};

const getImageUrl = (path) => {
  if (!path) {
    return "https://via.placeholder.com/300x450";
  }
  return `https://image.tmdb.org/t/p/w300${path}`;
};
</script>

<style scoped>

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  gap: 10px;
}

.pagination button {
  padding: 8px 12px;
  background-color: #333333;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.pagination button:hover {
  background-color: #ee9191;
}

.pagination button:disabled {
  background-color: #777777;
  cursor: not-allowed;
}

.pagination span {
  color: #ffffff;
  font-size: 16px;
}

/* 기존 에일 스타일 */
.ale-view {
  padding: 20px;
  background-color: #1e1e1e; /* 어두운 배경색 */
  color: #e8e8e8; /* 기본 텍스트 색상 */
  font-family: Arial, sans-serif;
}

/* 제목 스타일 */
h1 {
  text-align: center;
  color: #ffffff;
  margin-bottom: 30px;
}

.ale-intro {
  display: flex;
  align-items: center;
  margin-bottom: 40px;
}

.ale-image {
  width: 300px;
  height: auto;
  margin-right: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5); /* 그림자 어둡게 */
}

.ale-description {
  font-size: 16px;
  line-height: 1.8;
  flex: 1;
}

/* 에일과 영화 페어링 설명 */
.ale-action-pairing {
  margin-top: 20px;
  color: #dddddd; /* 밝은 회색 텍스트 */
  font-size: 15px;
}

/* 맥주 리스트 섹션 */
.beer-list h2 {
  color: #ffffff;
  margin-bottom: 20px;
}

.beer-card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.beer-card {
  background-color: #333333; /* 어두운 카드 배경색 */
  color: #ffffff; /* 밝은 텍스트 색상 */
  border-radius: 8px;
  padding: 20px;
  width: 20%;
  min-width: 250px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
  transition: transform 0.2s, box-shadow 0.2s;
}

.beer-card:hover {
  transform: scale(1.02);
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.7);
}

/* 영화 페어링 섹션 */
.movies-scroll {
  margin-top: 40px;
}

.movie-card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.movie-card {
  width: 150px;
  text-align: center;
}

.movie-poster {
  width: 100%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.7); /* 어두운 그림자 */
}

.movie-title {
  margin-top: 10px;
  font-size: 14px;
  color: #ffffff; /* 밝은 텍스트 색상 */
}
</style>
