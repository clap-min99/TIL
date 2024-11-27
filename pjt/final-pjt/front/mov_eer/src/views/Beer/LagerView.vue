<template>
  <div class="lager-view">
    <h1>🍺 라거(Lager)</h1>
    <div class="lager-intro">
      <img
        src="@/assets/Lager.png"
        alt="Lager Beer"
        class="lager-image"
      />
      <div class="lager-description">
        <p>
          <strong>라거(Lager)</strong>는 하부 발효 방식을 통해 만들어지는 맥주로, 낮은 온도에서 발효되어 깨끗하고 청량한 맛이 특징입니다.
          라거는 세계적으로 가장 대중적인 맥주 스타일로, 필스너, 둔켈, 헬레스 등 다양한 하위 유형이 있습니다.
        </p>
        <p>
          부드럽고 깔끔한 맛 덕분에 누구나 즐길 수 있는 맥주로, 전 세계 축제나 일상적인 모임에서 사랑받고 있습니다.
          더운 여름날의 갈증 해소부터 가벼운 식사와의 조화까지, 라거는 늘 좋은 선택입니다.
        </p>
        <p class="lager-adventure-pairing">
          🎥 라거는 Adventure(모험) 장르와 잘 어울립니다.
          라거 한 잔의 시원한 청량감은 모험 영화 속 흥미진진한 장면과 함께 완벽한 조화를 이룹니다.
        </p>
      </div>
    </div>

    <div class="beer-list">
      <h2>추천 Lager 리스트</h2>
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
      <h2>페어링 with Lager 🎥</h2>
      <div class="movie-card-container">
        <!-- 페이징된 영화 목록 -->
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
  return getBeerMovies('Lager').slice(start, end); // Lager 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getBeerMovies('Lager').length / itemsPerPage);
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
    name: "필스너 (Pilsner)",
    description: "가볍고 청량한 맛이 특징인 라거 스타일.",
    representativeBrands: "Pilsner Urquell, Heineken",
    style: "Pilsner",
    foodPairing: "샐러드, 가벼운 해산물 요리",
    foodEmoji: "🥗🦐"
  },
  {
    id: 2,
    name: "헬레스 (Helles)",
    description: "부드럽고 약간의 단맛이 느껴지는 독일 스타일 라거.",
    representativeBrands: "Augustiner Helles, Paulaner Original Münchner",
    style: "Helles",
    foodPairing: "치킨, 감자 요리",
    foodEmoji: "🍗🥔"
  },
  {
    id: 3,
    name: "둔켈 (Dunkel)",
    description: "깊고 진한 몰트 풍미가 특징인 어두운 라거.",
    representativeBrands: "Ayinger Altbairisch Dunkel, Warsteiner Dunkel",
    style: "Dunkel",
    foodPairing: "구운 고기, 치즈 플래터",
    foodEmoji: "🍖🧀"
  },
  {
    id: 4,
    name: "복 (Bock)",
    description: "묵직하고 강렬한 맛을 자랑하는 독일 라거 스타일.",
    representativeBrands: "Spaten Optimator, Celebrator Doppelbock",
    style: "Bock",
    foodPairing: "스테이크, 초콜릿 디저트",
    foodEmoji: "🥩🍫"
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

/* Lager 스타일 */
.lager-view {
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

.lager-intro {
  display: flex;
  align-items: center;
  margin-bottom: 40px;
}

.lager-image {
  width: 300px;
  height: auto;
  margin-right: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5); /* 그림자 어둡게 */
}

.lager-description {
  font-size: 16px;
  line-height: 1.8;
  flex: 1;
}

.lager-adventure-pairing {
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
