<template>
  <div class="irish-whiskey-view">
    <h1>🥃 Irish 위스키</h1>
    <div class="whiskey-intro">
      <img
        src="@/assets/Irish.png"
        alt="Irish Whiskey"
        class="whiskey-image"
      />
      <div class="whiskey-description">
        <p>
          <strong>Irish 위스키</strong>는 아일랜드에서 생산되는 위스키로, 삼중 증류 과정을 거쳐 부드럽고 깔끔한 풍미를 자랑합니다.
          몰트와 곡물을 혼합하여 만들어지며, 특유의 가벼운 맛과 향 덕분에 세계적으로 사랑받고 있습니다.
        </p>
        <p>
          Irish 위스키는 다른 위스키에 비해 스모키한 맛이 덜하고, 초심자부터 애호가까지 누구나 즐길 수 있는 매력을 가지고 있습니다.
          특히, 아일랜드 전통적인 문화와 함께 Irish 위스키를 즐기는 경험은 독특한 추억을 선사합니다.
        </p>
        <p class="irish-western-pairing">
          🍿 Irish 위스키는 Western(서부극) 장르와 완벽하게 어울립니다.
          대평원을 배경으로 펼쳐지는 카우보이들의 모험과 함께 Irish 위스키 한 잔으로 분위기를 더해보세요!
        </p>
      </div>
    </div>

    <div class="whiskey-list">
      <h2>추천 Irish 위스키 리스트</h2>
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
      <h2>페어링 with Irish 위스키 🥃</h2>
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
  return getWhiskeyMovies('Irish').slice(start, end); // Irish 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getWhiskeyMovies('Irish').length / itemsPerPage);
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
    name: "Jameson Irish Whiskey",
    description: "부드럽고 가볍게 스며드는 전통적인 아일랜드 위스키.",
    representativeBrands: "Jameson",
    region: "아일랜드",
    foodPairing: "치즈 플래터, 감자 요리",
    foodEmoji: "🧀🥔"
  },
  {
    id: 2,
    name: "Bushmills Original",
    description: "과일향과 허브향이 어우러진 크리미한 Irish 위스키.",
    representativeBrands: "Bushmills",
    region: "아일랜드",
    foodPairing: "훈제 연어, 크래커",
    foodEmoji: "🐟🍘"
  },
  {
    id: 3,
    name: "Redbreast 12 Year Old",
    description: "깊고 풍부한 맛과 크리미한 질감이 특징인 싱글 포트 스틸 위스키.",
    representativeBrands: "Redbreast",
    region: "아일랜드",
    foodPairing: "건포도, 초콜릿 디저트",
    foodEmoji: "🍇🍫"
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

/* Irish 위스키 스타일 */
.irish-whiskey-view {
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

.irish-western-pairing {
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
