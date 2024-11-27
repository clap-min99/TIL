<template>
  <div class="recommendation-container">
    <h2 class="recommendation-header">MVBeer 추천 주류🥂</h2>
    <div class="recommendation-card">
      <img :src="randomAlcohol.imageUrl" alt="Alcohol Image" class="alcohol-image" />
      <div class="recommendation-content">
        <h3 class="alcohol-name">{{ randomAlcohol?.name }}</h3>
        <p class="description">{{ randomAlcohol?.description }}</p>
        <p class="region">생산 지역: {{ randomAlcohol?.region }}</p>
        <p class="taste">맛: {{ randomAlcohol?.taste }}</p>
        <button @click="handleButtonClick" :class="['recommendation-button', { active: isButtonActive }]">다른 추천 보기</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAlcoholStore } from '@/stores/alcohol_select'; // Pinia 스토어 가져오기

// Pinia 스토어 사용
const alcoholStore = useAlcoholStore();

// 랜덤 주류 데이터 상태
const randomAlcohol = ref({}); // 초기값

// 모든 주류를 하나의 배열로 합치기
const allAlcohols = [
  ...alcoholStore.beers,
  ...alcoholStore.whisky || [], // whiskies가 존재하지 않으면 빈 배열 처리
  ...alcoholStore.wine || [], // wines가 존재하지 않으면 빈 배열 처리
];

// 랜덤 주류 선택 함수
const getRandomAlcohol = () => {
  const randomIndex = Math.floor(Math.random() * allAlcohols.length); // 랜덤 인덱스 생성
  randomAlcohol.value = allAlcohols[randomIndex]; // 랜덤 주류 설정
};

// 컴포넌트 로드 시 초기값 설정
getRandomAlcohol();

// 버튼 상태를 위한 ref
const isButtonActive = ref(false);

// 버튼 클릭 핸들러
const handleButtonClick = () => {
  isButtonActive.value = !isButtonActive.value; // 버튼 활성화 상태 토글
  getRandomAlcohol(); // 새로운 주류 추천
};
</script>

<style scoped>
/* 추천 주류 전체 컨테이너 */
.recommendation-container {
  background-image: url('@/assets/background-bar.jpg'); /* 배경 이미지 추가 */
  background-size: cover;
  background-position: center;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

/* 추천 헤더 스타일 */
.recommendation-header {
  text-align: center;
  color: #e8e8e8;
  font-size: 2rem;
  margin-bottom: 1.5rem;
}

/* 추천 카드 스타일 */
.recommendation-card {
  background-color: rgba(0, 0, 0, 0.8); /* 카드 배경 투명도 */
  border-radius: 15px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem;
  max-width: 500px;
  margin: 0 auto;
  transition: transform 0.3s, box-shadow 0.3s;
}

.recommendation-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7);
}

/* 주류 이미지 스타일 */
.alcohol-image {
  width: 100%;
  max-width: 300px;
  height: auto;
  border-radius: 10px;
  margin-bottom: 1rem;
}

/* 추천 내용 스타일 */
.recommendation-content {
  text-align: center;
  color: #f0f0f0;
}

.alcohol-name {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: #ffcc66; /* 강조된 색상 */
}

.description {
  margin-bottom: 0.5rem;
  color: #bfbfbf; /* 기울임 제거 */
}

.region,
.taste {
  margin-top: 0.5rem;
  font-weight: bold;
}

/* 추천 버튼 스타일 */
.recommendation-button {
  margin-top: 1rem;
  padding: 0.75rem 1.5rem;
  border: none;
  background-color: #3b3b3b; /* 초기 회색 버튼 색상 */
  color: #ffffff;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 25px;
  transition: background-color 0.3s, transform 0.3s;
}

.recommendation-button:hover {
  transform: translateY(-3px);
}

.recommendation-button:hover {
  background-color: #ff7373; /* 활성화된 상태의 분홍색 */
}
</style>
