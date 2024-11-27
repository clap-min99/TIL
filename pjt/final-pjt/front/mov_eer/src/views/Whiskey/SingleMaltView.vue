<template>
  <div class="singlemalt-whiskey-view">
    <h1>🥃 Single Malt 위스키</h1>
    <div class="whiskey-intro">
      <img
        src="@/assets/SingleMalt.png"
        alt="Single Malt Whiskey"
        class="whiskey-image"
      />
      <div class="whiskey-description">
        <p>
          <strong>Single Malt 위스키</strong>는 단일 증류소에서 생산된 보리만을 원료로 하는 위스키로,
          깊고 풍부한 맛과 향이 특징입니다. 각 증류소의 고유한 환경과 제조 방식 덕분에 
          서로 다른 개성을 지닌 위스키들이 탄생합니다.
        </p>
        <p>
          Single Malt는 위스키 애호가들에게 있어 특별한 매력을 가지며, 스트레이트로 마시거나
          약간의 물을 타서 즐기는 것이 일반적입니다. 독특한 풍미와 향은 고급스러움을 선사합니다.
        </p>
        <p class="singlemalt-thriller-pairing">
          🍿 Single Malt 위스키는 Thriller(스릴러) 장르와 잘 어울립니다.
          긴장감 넘치는 영화와 함께 복합적인 풍미의 위스키 한 잔은 몰입감을 배가시켜줍니다.
        </p>
      </div>
    </div>

    <div class="whiskey-list">
      <h2>추천 Single Malt 위스키 리스트</h2>
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
      <h2>페어링 with Single Malt 🥃</h2>
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
  return getWhiskeyMovies('SingleMalt').slice(start, end); // Single Malt 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getWhiskeyMovies('SingleMalt').length / itemsPerPage);
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
    name: "The Macallan Sherry Oak 12 Years Old",
    description: "건포도와 달콤한 시트러스 향이 어우러진 부드러운 맛.",
    representativeBrands: "The Macallan",
    region: "스코틀랜드 스페이사이드",
    foodPairing: "다크 초콜릿, 말린 과일",
    foodEmoji: "🍫🍇"
  },
  {
    id: 2,
    name: "Glenfiddich 18 Years Old",
    description: "오크와 달콤한 애플 향이 균형을 이루는 풍부한 풍미.",
    representativeBrands: "Glenfiddich",
    region: "스코틀랜드 하이랜드",
    foodPairing: "구운 고기, 체더 치즈",
    foodEmoji: "🥩🧀"
  },
  {
    id: 3,
    name: "Lagavulin 16 Years Old",
    description: "스모키함과 짭짤한 바다 내음이 조화로운 강렬한 맛.",
    representativeBrands: "Lagavulin",
    region: "스코틀랜드 아일라",
    foodPairing: "훈제 연어, 블루 치즈",
    foodEmoji: "🐟🧀"
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

/* Single Malt 위스키 스타일 */
.singlemalt-whiskey-view {
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
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5); /* 어두운 그림자 */
}

.whiskey-description {
  font-size: 16px;
  line-height: 1.8;
  flex: 1;
}

.singlemalt-thriller-pairing {
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
  background-color: #333333; /* 어두운 카드 배경 */
  color: #ffffff;
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
