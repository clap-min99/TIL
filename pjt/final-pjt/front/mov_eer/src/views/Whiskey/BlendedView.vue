<template>
  <div class="blended-whiskey-view">
    <h1>🥃 Blended 위스키</h1>
    <div class="whiskey-intro">
      <img
        src="@/assets/Blended.png"
        alt="Blended Whiskey"
        class="whiskey-image"
      />
      <div class="whiskey-description">
        <p>
          <strong>Blended 위스키</strong>는 다양한 싱글 몰트 위스키와 곡물 위스키를 혼합하여 만들어지는 술로,
          부드럽고 균형 잡힌 맛을 자랑합니다. 
          이 스타일은 대중적으로 가장 널리 사랑받으며, 각 브랜드마다 독특한 풍미와 향을 지니고 있습니다.
        </p>
        <p>
          Blended 위스키는 가볍고 부드러운 맛 덕분에 입문자들에게 특히 적합하며, 
          온더락, 스트레이트, 또는 칵테일 재료로도 다양하게 활용됩니다.
        </p>
        <p class="blended-history-pairing">
          🍿 Blended 위스키는 역사 장르 영화와 잘 어울립니다.
          풍부한 향과 복합적인 맛은 역사 속 인물과 사건을 돌아보며 음미하기에 완벽한 동반자입니다.
        </p>
      </div>
    </div>

    <div class="whiskey-list">
      <h2>추천 Blended 위스키 리스트</h2>
      <div class="whiskey-card-container">
        <div v-for="whiskey in whiskeys" :key="whiskey.id" class="whiskey-card">
          <h3>{{ whiskey.name }}</h3>
          <p>{{ whiskey.description }}</p>
          <p><strong>대표 브랜드:</strong> {{ whiskey.representativeBrands }}</p>
          <p><strong>지역:</strong> {{ whiskey.region }}</p>
          <p>
            <strong>추천 안주:</strong> {{ whiskey.foodPairing }}
            <span>{{ whiskey.foodEmoji }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="movies-scroll">
      <h2>페어링 with Blended 위스키 🥃</h2>
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
  return getWhiskeyMovies('Blended').slice(start, end); // Blended 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getWhiskeyMovies('Blended').length / itemsPerPage);
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


const whiskeys = [
  {
    id: 1,
    name: "Johnnie Walker Black Label",
    description: "스모키한 맛과 부드러운 풍미가 조화를 이룬 대표적인 블렌디드 위스키.",
    representativeBrands: "Johnnie Walker",
    region: "스코틀랜드",
    foodPairing: "초콜릿 디저트, 스테이크",
    foodEmoji: "🍫🥩"
  },
  {
    id: 2,
    name: "Chivas Regal 12",
    description: "풍부한 과일 향과 부드러운 바닐라 풍미를 지닌 클래식 위스키.",
    representativeBrands: "Chivas Regal",
    region: "스코틀랜드",
    foodPairing: "치즈 플래터, 구운 고기",
    foodEmoji: "🧀🍖"
  },
  {
    id: 3,
    name: "Ballantine’s Finest",
    description: "깔끔하고 균형 잡힌 맛이 특징으로, 초보자들에게 적합한 위스키.",
    representativeBrands: "Ballantine's",
    region: "스코틀랜드",
    foodPairing: "크래커, 훈제 연어",
    foodEmoji: "🧈🐟"
  }
];

const liquorStore = useLiquorStore();
const movieStore = useMovieStore();

onMounted(() => {
  liquorStore.getWhiskeys();
  movieStore.getMovies();
  movieStore.getGenres();
});

const getWhiskeyMovies = (subtype) => {
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

/* Blended 위스키 스타일 */
.blended-whiskey-view {
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

.whiskey-intro {
  display: flex;
  align-items: center;
  margin-bottom: 40px;
}

.whiskey-image {
  width: 300px;
  height: auto;
  margin-right: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5); /* 그림자 어둡게 */
}

.whiskey-description {
  font-size: 16px;
  line-height: 1.8;
  flex: 1;
}

.blended-history-pairing {
  margin-top: 20px;
  color: #dddddd; /* 밝은 회색 텍스트 */
  font-size: 15px;
}

/* 위스키 리스트 섹션 */
.whiskey-list h2 {
  color: #ffffff;
  margin-bottom: 20px;
}

.whiskey-card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.whiskey-card {
  background-color: #333333; /* 어두운 카드 배경색 */
  color: #ffffff; /* 밝은 텍스트 색상 */
  border-radius: 8px;
  padding: 20px;
  width: 20%;
  min-width: 250px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
  transition: transform 0.2s, box-shadow 0.2s;
}

.whiskey-card:hover {
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
