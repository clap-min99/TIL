<template>
  <div class="rye-whiskey-view">
    <h1>🥃 Rye 위스키</h1>
    <div class="whiskey-intro">
      <img
        src="@/assets/Rye.png"
        alt="Rye Whiskey"
        class="whiskey-image"
      />
      <div class="whiskey-description">
        <p>
          <strong>Rye 위스키</strong>는 호밀(Rye)을 주재료로 만들어지는 위스키로, 특유의 강렬하고 스파이시한 풍미가 특징입니다.
          이 위스키는 높은 비율의 호밀을 사용하며, 그 덕분에 독특한 풍미와 깊이를 가지고 있습니다.
        </p>
        <p>
          미국과 캐나다에서 특히 인기 있는 Rye 위스키는 칵테일의 베이스로도 자주 사용됩니다.
          복합적인 향과 매혹적인 맛은 많은 위스키 애호가들의 마음을 사로잡았습니다.
        </p>
        <p class="rye-mystery-pairing">
          🍿 Rye 위스키는 Mystery(미스터리) 장르와 완벽하게 어울립니다.
          강렬하고 스파이시한 맛은 미스터리한 영화의 복잡한 플롯과 어우러져 몰입감을 극대화시킵니다.
        </p>
      </div>
    </div>

    <div class="whiskey-list">
      <h2>추천 Rye 위스키 리스트</h2>
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
      <h2>페어링 with Rye 위스키 🥃</h2>
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
  return getWhiskeyMovies('Rye').slice(start, end); // Rye 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getWhiskeyMovies('Rye').length / itemsPerPage);
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
    name: "Bulleit Rye",
    description: "95% 호밀로 만들어진 강렬한 스파이시함과 복합적인 풍미를 자랑.",
    representativeBrands: "Bulleit",
    region: "미국",
    foodPairing: "스모크 치즈, 치킨 윙",
    foodEmoji: "🧀🍗"
  },
  {
    id: 2,
    name: "Templeton Rye",
    description: "미디엄 바디와 은은한 과일향을 지닌 전통적인 Rye 위스키.",
    representativeBrands: "Templeton",
    region: "미국",
    foodPairing: "크래커, 견과류",
    foodEmoji: "🍪🥜"
  },
  {
    id: 3,
    name: "Canadian Club 100% Rye",
    description: "캐나다산 100% 호밀로 만들어져 부드럽고 스파이시한 맛을 겸비.",
    representativeBrands: "Canadian Club",
    region: "캐나다",
    foodPairing: "BBQ 립, 다크 초콜릿",
    foodEmoji: "🍖🍫"
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

/* Rye 위스키 스타일 */
.rye-whiskey-view {
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

.rye-mystery-pairing {
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
