<template>
  <div class="lager-view">
    <h1>🍺 필스너(Pilsner)</h1>
    <div class="lager-intro">
      <img
        src="@/assets/Pilsner.png"
        alt="Pilsner Beer"
        class="lager-image"
      />
      <div class="lager-description">
        <p>
          <strong>필스너(Pilsner)</strong>는 맑고 청량한 맛이 특징인 하부 발효 방식의 라거 맥주입니다.
          체코의 필젠 지역에서 유래한 이 맥주는 황금빛 색상과 부드러운 홉의 쓴맛으로 많은 사람들에게 사랑받고 있습니다.
        </p>
        <p>
          필스너는 전 세계에서 가장 대중적인 맥주 스타일 중 하나로, 깨끗한 맛과 시원한 탄산감 덕분에 더운 날씨에 특히 잘 어울립니다.
          축구 경기나 야외 파티 같은 순간에 필스너 한 잔은 최고의 선택이 될 것입니다.
        </p>
        <p class="lager-comedy-pairing">
          🍿 필스너는 코미디 영화와 환상적인 조합을 이룹니다.
          가볍고 청량한 필스너 한 잔은 영화 속 유쾌한 장면과 함께 즐거움을 배가시켜줍니다.
          친구들과 함께 웃음 가득한 시간을 보내보세요!
        </p>
      </div>
    </div>

    <div class="beer-list">
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
      <h2>페어링 with 필스너🍺</h2>
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
  return getBeerMovies('Pilsner').slice(start, end); // Pilsner 기준으로 변경
});

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(getBeerMovies('Pilsner').length / itemsPerPage);
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
    name: "필스너 우르켈 (Pilsner Urquell)",
    description: "황금빛 맥주로 부드러운 몰트와 적당한 홉의 쓴맛이 특징입니다.",
    representativeBrands: "Pilsner Urquell, Heineken",
    style: "Pilsner",
    foodPairing: "샐러드, 가벼운 해산물 요리",
    foodEmoji: "🥗🦐"
  },
  {
    id: 2,
    name: "하이네켄 (Heineken)",
    description: "가볍고 청량한 맛으로 누구나 즐길 수 있는 필스너 맥주.",
    representativeBrands: "Heineken",
    style: "Pilsner",
    foodPairing: "나초, 감자튀김",
    foodEmoji: "🌮🍟"
  },
  {
    id: 3,
    name: "스타 프라하멘 (Staropramen)",
    description: "체코 스타일의 전통 필스너로 균형 잡힌 홉과 몰트의 맛이 돋보입니다.",
    representativeBrands: "Staropramen",
    style: "Pilsner",
    foodPairing: "구운 고기, 바비큐",
    foodEmoji: "🍖🍗"
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

/* 필스너 스타일 */
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

.lager-comedy-pairing {
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
