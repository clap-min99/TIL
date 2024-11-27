<template>
  <div class="bourbon-whiskey-view">
    <h1>🥃 Bourbon 위스키</h1>
    <div class="whiskey-intro">
      <img
        src="@/assets/Bourbon.png"
        alt="Bourbon Whiskey"
        class="whiskey-image"
      />
      <div class="whiskey-description">
        <p>
          <strong>Bourbon 위스키</strong>는 미국에서 주로 생산되는 위스키로, 주로 옥수수를 주재료로 만들어집니다.
          특유의 달콤한 향과 풍미, 그리고 캐러멜과 바닐라의 뉘앙스가 특징입니다.
        </p>
        <p>
          Bourbon은 미국의 켄터키 지역에서 특히 유명하며, 최소 51% 이상의 옥수수로 만들어지고,
          새 오크통에서 숙성되어 깊고 풍부한 맛을 자랑합니다.
          부드러우면서도 복합적인 풍미는 세계적으로 많은 팬을 보유하고 있습니다.
        </p>
        <p class="bourbon-animation-pairing">
          🍿 Bourbon 위스키는 Animation(애니메이션) 장르와 환상적으로 어울립니다.
          창의적이고 다채로운 애니메이션 작품과 함께 달콤하고 부드러운 Bourbon 한 잔을 즐겨보세요!
        </p>
      </div>
    </div>

    <div class="whiskey-list">
      <h2>추천 Bourbon 위스키 리스트</h2>
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
      <h2>페어링 with Bourbon 위스키 🥃</h2>
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
  return getWhiskeyMovies('Bourbon').slice(start, end); // Bourbon 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getWhiskeyMovies('Bourbon').length / itemsPerPage);
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
    name: "Jim Beam",
    description: "가장 대표적인 Bourbon으로 달콤한 바닐라와 캐러멜 풍미가 특징.",
    representativeBrands: "Jim Beam",
    region: "미국 켄터키",
    foodPairing: "바베큐, 버거",
    foodEmoji: "🍖🍔"
  },
  {
    id: 2,
    name: "Maker's Mark",
    description: "부드럽고 달콤하며 과일과 바닐라 향이 어우러진 Bourbon.",
    representativeBrands: "Maker's Mark",
    region: "미국 켄터키",
    foodPairing: "스모크드 치킨, 초콜릿 디저트",
    foodEmoji: "🍗🍫"
  },
  {
    id: 3,
    name: "Woodford Reserve",
    description: "깊고 복합적인 맛과 향을 자랑하는 프리미엄 Bourbon.",
    representativeBrands: "Woodford Reserve",
    region: "미국 켄터키",
    foodPairing: "구운 스테이크, 브라우니",
    foodEmoji: "🥩🍪"
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

/* Bourbon 위스키 스타일 */
.bourbon-whiskey-view {
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

.bourbon-animation-pairing {
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
