<template>
  <div class="red-wine-view">
    <h1>🍷 Red 와인</h1>
    <div class="wine-intro">
      <img
        src="@/assets/RedWine.png"
        alt="Red Wine"
        class="wine-image"
      />
      <div class="wine-description">
        <p>
          <strong>Red 와인</strong>은 포도의 껍질과 함께 발효되어 풍부한 색감과 깊은 풍미를 지닌 와인입니다.
          다양한 품종과 지역적 특성에 따라 고유한 향과 맛을 가지고 있으며, 대개 육류와 잘 어울리는 와인으로 알려져 있습니다.
        </p>
        <p>
          레드 와인은 그 자체로도 훌륭하지만, 특별한 저녁식사나 감동적인 드라마를 감상할 때 더욱 빛을 발합니다.
          피노 누아(Pinot Noir), 카베르네 소비뇽(Cabernet Sauvignon), 멀롯(Merlot) 등이 대표적인 레드 와인 품종입니다.
        </p>
        <p class="red-drama-pairing">
          🍿 Red 와인은 Drama(드라마) 장르와 잘 어울립니다.
          깊이 있는 와인의 풍미는 감동적인 이야기와 완벽한 조화를 이룹니다. 와인 한 잔과 함께 진한 여운을 즐겨보세요.
        </p>
      </div>
    </div>

    <div class="wine-list">
      <h2>추천 Red 와인 리스트</h2>
      <div class="wine-card-container">
        <div v-for="wine in wines" :key="wine.id" class="wine-card">
          <h3>{{ wine.name }}</h3>
          <p>{{ wine.description }}</p>
          <p><strong>대표 브랜드:</strong> {{ wine.representativeBrands }}</p>
          <p><strong>추천 안주:</strong> {{ wine.foodPairing }}</p>
          <p>
            <span>{{ wine.foodEmoji }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="movies-scroll">
      <h2>페어링 with Red 🍷</h2>
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
  return getWineMovies('Red').slice(start, end); // Red Wine 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getWineMovies('Red').length / itemsPerPage);
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
    name: "Cabernet Sauvignon",
    description: "풍부한 타닌과 블랙베리 향이 돋보이는 풀바디 와인.",
    representativeBrands: "Robert Mondavi, Penfolds",
    foodPairing: "스테이크, 양고기",
    foodEmoji: "🥩🐑"
  },
  {
    id: 2,
    name: "Pinot Noir",
    description: "부드럽고 과일 향이 강한 미디엄 바디 와인.",
    representativeBrands: "Louis Jadot, Cloudy Bay",
    foodPairing: "구운 연어, 치즈 플래터",
    foodEmoji: "🐟🧀"
  },
  {
    id: 3,
    name: "Merlot",
    description: "매끄럽고 부드러운 구조를 가진 와인으로 초보자에게 적합.",
    representativeBrands: "Duckhorn, Chateau Petrus",
    foodPairing: "치즈 플래터, 초콜릿 디저트",
    foodEmoji: "🧀🍫"
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

/* Red 와인 스타일 - 어두운 테마 */
.red-wine-view {
  padding: 20px;
  background-color: #1e1e1e; /* 어두운 배경 */
  color: #e8e8e8; /* 텍스트 색상 */
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #ffffff;
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
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5); /* 어두운 그림자 */
}

.wine-description {
  font-size: 16px;
  line-height: 1.8;
  flex: 1;
}

.red-drama-pairing {
  margin-top: 20px;
  color: #dddddd; /* 밝은 회색 텍스트 */
  font-size: 15px;
}

/* 와인 리스트 섹션 */
.wine-list h2 {
  color: #ffffff;
  margin-bottom: 20px;
}

.wine-card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.wine-card {
  background-color: #333333; /* 어두운 카드 배경 */
  color: #ffffff;
  border-radius: 8px;
  padding: 20px;
  width: 20%;
  min-width: 250px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
  transition: transform 0.2s, box-shadow 0.2s;
}

.wine-card:hover {
  transform: scale(1.02);
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.7);
}

/* 영화 섹션 */
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
