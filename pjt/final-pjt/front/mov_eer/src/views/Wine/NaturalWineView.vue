<template>
  <div class="natural-wine-view">
    <h1>🍇 Natural 와인</h1>
    <div class="wine-intro">
      <img
        src="@/assets/NaturalWine.png"
        alt="Natural Wine"
        class="wine-image"
      />
      <div class="wine-description">
        <p>
          <strong>Natural 와인</strong>은 인위적인 화학물질 사용 없이 자연적으로 생산된 와인으로, 
          유기농 포도를 사용하며 발효 과정에서도 인공 첨가물을 배제하는 것이 특징입니다.
        </p>
        <p>
          자연 그대로의 맛과 향을 담은 Natural 와인은 현대 와인 애호가들에게 큰 인기를 끌고 있습니다.
          독특한 풍미와 신선함을 느낄 수 있으며, 와인을 통해 자연과의 연결을 경험할 수 있습니다.
        </p>
        <p class="natural-documentary-pairing">
          📽️ Natural 와인은 Documentary(다큐멘터리)와 완벽한 페어링을 이룹니다.
          자연의 정수를 담은 와인 한 잔과 함께 다큐멘터리를 감상하며 세상과 자연에 대해 깊이 있는 시선을 가져보세요.
        </p>
      </div>
    </div>

    <div class="wine-list">
      <h2>추천 Natural 와인 리스트</h2>
      <div class="wine-card-container">
        <div v-for="wine in wines" :key="wine.id" class="wine-card">
          <h3>{{ wine.name }}</h3>
          <p>{{ wine.description }}</p>
          <p><strong>대표 브랜드:</strong> {{ wine.representativeBrands }}</p>
          <p><strong>추천 페어링:</strong> {{ wine.foodPairing }}</p>
          <p>
            <span>{{ wine.foodEmoji }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="movies-scroll">
      <h2>페어링 with Natural Wine 📽️</h2>
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
  return getWineMovies('Natural').slice(start, end); // Natural Wine 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getWineMovies('Natural').length / itemsPerPage);
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


const wines = [
  {
    id: 1,
    name: "Les Vins Pirouettes",
    description: "프랑스 알자스 지역의 순수 자연 와인으로 신선한 과일 향이 특징.",
    representativeBrands: "Domaine Binner",
    foodPairing: "채소 요리, 신선한 샐러드",
    foodEmoji: "🥗🍅"
  },
  {
    id: 2,
    name: "Radikon",
    description: "이탈리아에서 생산된 오렌지 와인으로 독특한 풍미와 텍스처를 자랑.",
    representativeBrands: "Radikon",
    foodPairing: "훈제 연어, 치즈",
    foodEmoji: "🐟🧀"
  },
  {
    id: 3,
    name: "Gut Oggau",
    description: "오스트리아의 대표적인 내추럴 와인 브랜드로 독특한 라벨 디자인이 돋보임.",
    representativeBrands: "Gut Oggau",
    foodPairing: "구운 야채, 곡물 요리",
    foodEmoji: "🌽🍠"
  }
];

const liquorStore = useLiquorStore();
const movieStore = useMovieStore();

onMounted(() => {
  liquorStore.getWines();
  movieStore.getMovies();
  movieStore.getGenres();
});

const getWineMovies = (subtype) => {
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
h2{
  color:  #ffffff
}

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

/* Natural 와인 스타일 - 어두운 테마 */
.natural-wine-view {
  padding: 20px;
  background-color: #1a1a1a; /* 어두운 배경 */
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #ffffff; /* 흰색 텍스트 */
  margin-bottom: 30px;
}

.wine-intro {
  display: flex;
  align-items: center;
  margin-bottom: 40px;
}

.wine-image {
  width: 300px;
  height: auto;
  margin-right: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(255, 255, 255, 0.1);
}

.wine-description {
  color: #cccccc; /* 연한 회색 */
  font-size: 16px;
  line-height: 1.8;
  flex: 1;
}

.natural-documentary-pairing {
  margin-top: 20px;
  font-style: italic;
  color: #999999; /* 더 어두운 회색 */
  font-size: 15px;
}

.wine-list h2 {
  color: #ffffff; /* 흰색 텍스트 */
  margin-bottom: 20px;
}

.wine-card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.wine-card {
  background-color: #333333; /* 어두운 카드 배경 */
  border-radius: 8px;
  padding: 20px;
  width: 20%;
  min-width: 250px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
  transition: transform 0.2s, box-shadow 0.2s;
}

.wine-card:hover {
  transform: scale(1.02);
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.6);
}

h3 {
  color: #ffffff; /* 흰색 텍스트 */
  margin-bottom: 10px;
}

p {
  color: #cccccc; /* 연한 회색 텍스트 */
  margin: 5px 0;
  line-height: 1.6;
}

/* 영화 스타일 */
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
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.movie-title {
  margin-top: 10px;
  font-size: 14px;
  color: #ffffff; /* 흰색 텍스트 */
}
</style>
