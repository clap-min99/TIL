<template>
  <div class="container">
    <div class="background-image"></div> <!-- 배경 -->
    <div class="content">
      <HeaderComponent />
      <RouterView />
    </div>

    <!-- 스크롤 버튼 -->
    <div class="scroll-buttons">
      <button @click="scrollToTop"> ⬆ </button>
      <button @click="scrollToBottom"> ⬇ </button>
    </div>
  </div>
</template>



<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useMovieStore } from './stores/movie';
import HeaderComponent from './components/shared/HeaderComponent.vue';
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import LoginView from './views/LoginView.vue';
import { useLogStore } from './stores/log'

// 위로 스크롤하는 함수
const scrollToTop = () => {
  window.scrollTo({
    top: 0, // 화면 최상단
    behavior: 'smooth', // 부드럽게 스크롤
  });
};

// 아래로 스크롤하는 함수
const scrollToBottom = () => {
  window.scrollTo({
    top: document.documentElement.scrollHeight, // 문서의 전체 높이
    behavior: 'smooth', // 부드럽게 스크롤
  });
};

</script>

<style scoped>
nav {
  display: flex;
  gap: 10px;
  margin: 10px 0;
}


.container {
  position: relative;
  width: 100%;
  height: 100%;
}

.background-image {
  position: fixed; /* 스크롤에도 고정 */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/back.png'); /* 배경 이미지 경로 */
  background-size: cover;
  background-position: center;
  z-index: -1; /* 배경을 콘텐츠 뒤로 */
  filter: brightness(0.4); /* 약간 어둡게 처리 */
  opacity: 0.8; /* 투명도 조정 */
}

.content {
  position: relative;
  z-index: 1; /* 콘텐츠를 배경 위로 배치 */
}


.scroll-buttons {
  position: fixed;
  bottom: 20px;
  right: 20px;
  display: flex;
  flex-direction: column;
  gap: 15px;
  z-index: 9999; /* 항상 최상단에 표시 */
}

.scroll-buttons button {
  background-color: transparent; /* 배경 제거 */
  color: white; /* 화살표 색상 */
  border: none; /* 테두리 제거 */
  font-size: 24px; /* 화살표 크기 */
  cursor: pointer;
  transition: color 0.3s ease; /* 호버 효과 */
  text-decoration: none; /* 밑줄 제거 */
}

.scroll-buttons button:hover {
  color: #ee9191; /* 호버 시 색상 변경 */
}

.scroll-buttons button:focus {
  outline: none; /* 포커스 시 외곽선 제거 */
}

</style>