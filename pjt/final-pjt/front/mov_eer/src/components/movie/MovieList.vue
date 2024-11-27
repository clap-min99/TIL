<template>
  <div class="background-container">
    <div class="carousel-container">
      <div class="carousel">
        <div
          v-for="(movie, index) in filteredMovies"
          :key="movie.id"
          class="carousel-item"
          :style="getItemStyle(index)"
        >
          <MovieMainInfo :movie="movie" />
        </div>
      </div>
      <button class="arrow left" @click="prevSlide">‹</button>
      <button class="arrow right" @click="nextSlide">›</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import MovieMainInfo from "./MovieMainInfo.vue";

const store = useMovieStore();
const currentIndex = ref(0);
const radius = 600; // 캐러셀 반지름

// 원하는 movie_id 배열
const desiredMovieIds = [ 912649, 1100782, 1184918, 558449, 1034541, 791042, 1118031, 402431, 533535 ]; // 원하는 영화 ID

// store에서 movies를 가져오고 desiredMovieIds로 필터링
const filteredMovies = computed(() => {
  return store.movies.filter((movie) => desiredMovieIds.includes(movie.id));
});

// 데이터 로드 (movies가 비어있을 경우 로드)
onMounted(() => {
  if (!store.movies.length) {
    store.getMovies(); // Pinia 스토어에서 movies를 가져옴
  }
});

// 영화 슬라이드 스타일 계산
const getItemStyle = (index) => {
  const total = filteredMovies.value.length;
  const angle = ((index - currentIndex.value + total) % total) * (360 / total);
  return {
    transform: `rotateY(${angle}deg) translateZ(${radius}px)`,
    opacity: index === currentIndex.value ? 1 : 0.5,
    zIndex: index === currentIndex.value ? 2 : 1,
    transition: "transform 0.5s ease, opacity 0.5s ease",
  };
};

// 이전 슬라이드
const prevSlide = () => {
  currentIndex.value =
    (currentIndex.value - 1 + filteredMovies.value.length) %
    filteredMovies.value.length;
};

// 다음 슬라이드
const nextSlide = () => {
  currentIndex.value =
    (currentIndex.value + 1) % filteredMovies.value.length;
};
</script>

<style scoped>
/* 기존 스타일 그대로 유지 */
.background-container {
  position: relative;
  background-image: url('@/assets/back.'); /* 배경 이미지 경로 */
  background-size: cover;
  background-position: center;
  padding: 50px 0;
  margin-bottom: 60px;
}

.carousel-container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  perspective: 1500px;
  height: 400px;
  margin-top: 160px;
  transform: translateX(-200px);
}

.carousel {
  display: flex;
  position: relative;
  transform-style: preserve-3d;
  width: 500%;
  height: 100%;
}

.carousel-item {
  position: absolute;
  width: 250px;
  height: 350px;
  border-radius: 8px;
  overflow: hidden;
  transform-origin: center;
}

.arrow {
  background: none;
  border: none;
  font-size: 2.5rem;
  cursor: pointer;
  color: #ccc;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
}

.arrow.left {
  left: -70px;
}

.arrow.right {
  right: -500px;
}

.arrow:hover {
  color: #fff;
}
</style>
