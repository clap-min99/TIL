<template>
  <div class="search-results-page">
    <h2>"{{ searchQuery }}"에 대한 검색 결과</h2>
    <div v-if="loading">검색 중...</div>
    <div v-else-if="searchResults.length" class="results-container">
      <div 
        v-for="(movie, index) in searchResults" 
        :key="index" 
        class="movie-card"
      >
        <RouterLink :to="{ name: 'MovieDetailView', params: { moviePk: movie.id } }">
          <img :src="getImageUrl(movie.poster_url)" class="movie-poster" :alt="movie.title" />
        </RouterLink>
        <p class="movie-title">{{ movie.title }}</p>
      </div>
    </div>
    <div v-else>
      <p>검색 결과가 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

// API URL 정의
const API_URL = 'http://127.0.0.1:8000'; // API 기본 URL

// 상태 정의
const route = useRoute();
const router = useRouter();
const searchQuery = ref(route.query.q || '');
const searchResults = ref([]);
const loading = ref(false);

// 영화 포스터 URL 생성 함수
const getImageUrl = (path) => {
  if (!path) {
    return 'https://via.placeholder.com/300x450'; // 기본 이미지
  }
  return `https://image.tmdb.org/t/p/w500${path}`;
};

// 검색 API 호출 함수
const fetchSearchResults = async () => {
  if (!searchQuery.value.trim()) {
    searchResults.value = [];
    return;
  }

  loading.value = true;

  try {
    // Axios를 사용해 API 호출
    const response = await axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/search/`,
      params: { q: searchQuery.value },
    });
    searchResults.value = response.data || [];
  } catch (error) {
    console.error('검색 실패:', error);
    searchResults.value = [];
  } finally {
    loading.value = false;
  }
};

// 검색 버튼 클릭 시 검색 실행 함수
const handleSearch = () => {
  if (!searchQuery.value.trim()) {
    alert('검색어를 입력해주세요.');
    return;
  }

  // 검색어와 함께 현재 URL 업데이트 및 검색 실행
  router.push({
    name: 'SearchResultsView',
    query: { q: searchQuery.value }
  });

  fetchSearchResults();
};

// 컴포넌트가 마운트되었을 때 검색 API 호출
onMounted(() => {
  fetchSearchResults();
});

// URL 쿼리 변경 감지
watch(() => route.query.q, (newQuery) => {
  searchQuery.value = newQuery || '';
  fetchSearchResults();
});
</script>

<style scoped>
.search-results-page {
  padding: 20px;
}

.search-container {
  position: relative;
  max-width: 400px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.search-bar {
  width: 100%;
  padding: 8px 10px;
  font-size: 1rem;
  border: 1px solid #444;
  border-radius: 4px;
  background-color: #3b3b3b;
  color: #f8f8f8;
}

.search-bar::placeholder {
  color: #bfbfbf;
}

.wine-image {
  width: 40px;
  height: auto;
  cursor: pointer;
}

h2 {
  color: #ee9191;
  margin-bottom: 20px;
}

.results-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.movie-card {
  width: 150px;
  text-align: center;
  cursor: pointer;
}

.movie-poster {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.movie-title {
  margin-top: 10px;
  font-size: 14px;
  color: #333;
  font-weight: bold;
}
</style>
