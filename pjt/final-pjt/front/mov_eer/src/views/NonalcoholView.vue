<template>
  <div class="nonalcohol-view">
    <h1>🥤논알콜(Non-Alcoholic)</h1>
    <div class="nonalcohol-intro">
      <img
        src="@/assets/nonalcohol.png"
        alt="Non-Alcoholic Drinks"
        class="nonalcohol-image"
      />
      <div class="nonalcohol-description">
        <p>
          <strong>논알콜(Non-Alcoholic)</strong>은 알코올을 포함하지 않는 음료로, 맥주와 칵테일의 대안으로 많은 사람들에게 사랑받고 있습니다.
          논알콜 음료는 건강을 생각하는 사람들 또는 운전을 해야 하는 사람들에게 적합한 선택입니다.
        </p>
        <p>
          논알콜 음료는 탄산음료, 무알콜 맥주, 무알콜 칵테일(Mocktail) 등 다양한 종류로 제공됩니다.
          또한, 다양한 상황에서 즐길 수 있도록 여러 맛과 스타일이 존재합니다.
        </p>
        <p class="nonalcohol-action-pairing">
          🥤 논알콜 음료는 가족 영화와 완벽한 조화를 이룹니다.
          편안한 분위기에서 온 가족이 함께 즐길 수 있는 최고의 선택입니다.
        </p>
      </div>
    </div>

    <div class="nonalcohol-list">
      <h2>추천 논알콜 음료</h2>
      <div class="nonalcohol-card-container">
        <div v-for="drink in drinks" :key="drink.id" class="nonalcohol-card">
          <h3>{{ drink.name }}</h3>
          <p>{{ drink.description }}</p>
          <p><strong>브랜드:</strong> {{ drink.representativeBrands }}</p>
          <p><strong>종류:</strong> {{ drink.style }}</p>
          <p>
            <strong>추천 음식:</strong> {{ drink.foodPairing }}
            <span>{{ drink.foodEmoji }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="movies-scroll">
      <h2>페어링 with 논알콜🥤</h2>
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
  return getNonAlcoholMovies('nonalcohol').slice(start, end); // Non-Alcohol 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getNonAlcoholMovies('nonalcohol').length / itemsPerPage);
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


const drinks = [
  {
    id: 1,
    name: "탄산음료",
    description: "청량감 넘치는 무알콜 탄산음료.",
    representativeBrands: "코카콜라, 스프라이트",
    style: "Soda",
    foodPairing: "팝콘, 핫도그",
    foodEmoji: "🍿🌭"
  },
  {
    id: 2,
    name: "무알콜 맥주",
    description: "맥주의 풍미를 그대로 살린 무알콜 맥주.",
    representativeBrands: "하이네켄 0.0, 칼스버그 알콜프리",
    style: "Non-Alcoholic Beer",
    foodPairing: "피자, 감자튀김",
    foodEmoji: "🍕🍟"
  },
  {
    id: 3,
    name: "무알콜 칵테일(Mocktail)",
    description: "칵테일의 맛을 즐길 수 있는 무알콜 버전.",
    representativeBrands: "바텐더의 창작 음료",
    style: "Mocktail",
    foodPairing: "샐러드, 치즈 플래터",
    foodEmoji: "🥗🧀"
  }
];

const liquorStore = useLiquorStore();
const movieStore = useMovieStore();

onMounted(() => {
  liquorStore.getNonalcohols(); // Nonalcohol 데이터 호출
  movieStore.getMovies();
  movieStore.getGenres();
});

const getNonAlcoholMovies = (subtype) => {
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

/* 논알콜 스타일 - 어두운 테마 */
.nonalcohol-view {
  padding: 20px;
  background-color: #1a1a1a; /* 어두운 배경 */
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #ffffff; /* 흰색 텍스트 */
  margin-bottom: 30px;
}

.nonalcohol-intro {
  display: flex;
  align-items: center;
  margin-bottom: 40px;
}

.nonalcohol-image {
  width: 300px;
  height: auto;
  margin-right: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(255, 255, 255, 0.1);
}

.nonalcohol-description {
  color: #cccccc; /* 연한 회색 */
  font-size: 16px;
  line-height: 1.8;
  flex: 1;
}

.nonalcohol-action-pairing {
  margin-top: 20px;
  font-style: italic;
  color: #999999; /* 어두운 회색 */
  font-size: 15px;
}

.nonalcohol-list h2 {
  color: #ffffff; /* 흰색 텍스트 */
  margin-bottom: 20px;
}

.nonalcohol-card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.nonalcohol-card {
  background-color: #333333; /* 어두운 카드 배경 */
  border-radius: 8px;
  padding: 20px;
  width: 20%;
  min-width: 250px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
  transition: transform 0.2s, box-shadow 0.2s;
}

.nonalcohol-card:hover {
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

h2{
  color:  #ffffff
}
</style>
