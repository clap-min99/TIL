<template>
  <div class="wheat-view">
    <h1>🍺 위트(Wheat)</h1>
    <div class="wheat-intro">
      <img
        src="@/assets/Wheat.png"
        alt="Wheat Beer"
        class="wheat-image"
      />
      <div class="wheat-description">
        <p>
          <strong>위트(Wheat)</strong>는 밀을 주원료로 사용하는 맥주로, 부드럽고 가벼운 풍미가 특징입니다.
          일반적으로 상큼한 과일 향과 은은한 산미를 느낄 수 있어 여름철 시원하게 즐기기 좋습니다.
        </p>
        <p>
          위트 맥주는 벨기에식(Belgian Witbier)과 독일식(Weissbier)으로 나뉘며, 각기 다른 매력을 제공합니다.
          벨기에식은 오렌지 껍질과 고수 같은 향신료를 사용하는 것이 특징이고, 독일식은 효모에서 오는 바나나 향과 부드러운 질감이 돋보입니다.
        </p>
        <p class="wheat-tvmovie-pairing">
          🍿 위트 맥주는 TV 영화와 훌륭한 페어링을 자랑합니다.
          가벼운 한 모금의 위트 맥주는 영화 감상 중의 편안함과 여유를 더해줍니다.
          부드러운 맥주와 함께 소소한 즐거움을 만끽해보세요!
        </p>
      </div>
    </div>

    <div class="beer-list">
      <h2>위트 맥주 리스트</h2>
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
      <h2>페어링 with 위트🍺</h2>
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
  return getBeerMovies('Wheat').slice(start, end); // Pilsner 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getBeerMovies('Wheat').length / itemsPerPage);
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
    name: "벨지안 위트비어 (Belgian Witbier)",
    description: "고수와 오렌지 껍질이 들어가 상큼한 맛과 향이 특징인 맥주.",
    representativeBrands: "Hoegaarden, Blue Moon",
    style: "Belgian Witbier",
    foodPairing: "가벼운 샐러드, 구운 닭고기",
    foodEmoji: "🥗🍗"
  },
  {
    id: 2,
    name: "독일 바이젠 (Weissbier)",
    description: "바나나와 정향의 향이 풍부한 부드러운 맥주.",
    representativeBrands: "Paulaner, Franziskaner",
    style: "Weissbier",
    foodPairing: "소시지, 프레첼",
    foodEmoji: "🌭🥨"
  },
  {
    id: 3,
    name: "아메리칸 위트비어 (American Wheat Beer)",
    description: "라이트 바디와 부드러운 산미가 돋보이는 미국식 밀 맥주.",
    representativeBrands: "Goose Island 312, Widmer Hefeweizen",
    style: "American Wheat",
    foodPairing: "타코, 나초",
    foodEmoji: "🌮🧀"
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

/* 위트 스타일 */
.wheat-view {
  padding: 20px;
  background-color: #1e1e1e; /* 어두운 배경색 */
  color: #e8e8e8; /* 기본 텍스트 색상 */
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #ffffff;
  margin-bottom: 30px;
}

.wheat-intro {
  display: flex;
  align-items: center;
  margin-bottom: 40px;
}

.wheat-image {
  width: 300px;
  height: auto;
  margin-right: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5); /* 그림자 어둡게 */
}

.wheat-description {
  font-size: 16px;
  line-height: 1.8;
  flex: 1;
}

.wheat-tvmovie-pairing {
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
