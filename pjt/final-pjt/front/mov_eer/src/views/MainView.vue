<template>
  <div class="main-container">
    <!-- 전체 배경 이미지 -->
    <div class="background-image"></div>
    <!-- 콘텐츠 -->
    <div class="content">
      <MovieList />
      <AlcoholMain />
      <Recommend />
    </div>
  </div>
</template>

<script setup>
import MovieList from "@/components/movie/MovieList.vue";
import AlcoholMain from "@/components/alcohol/AlcoholMain.vue";
import { onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import Recommend from "@/components/alcohol/Recommend.vue";

const store = useMovieStore();

onMounted(() => {
  store.getMovies();
});
</script>

<style scoped>
/* 메인 컨테이너 */
.main-container {
  position: relative;
  width: 100%;
  min-height: 100vh; /* 화면의 최소 높이 */
  overflow-x: hidden; /* 가로 스크롤 제거 */
  overflow-y: auto; /* 세로 스크롤 활성화 */
}

/* 배경 이미지 */
.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/back.png'); /* 배경 이미지 경로 */
  background-size: cover;
  background-position: center;
  z-index: -1; /* 배경이 콘텐츠 뒤로 */
  filter: brightness(0.4); /* 약간 어둡게 처리 */
}

/* 콘텐츠 */
.content {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 40px;
}
</style>
