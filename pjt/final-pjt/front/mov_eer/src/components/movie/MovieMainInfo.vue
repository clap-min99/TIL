<template>
  <div class="card">
    <RouterLink :to="{ name: 'MovieDetailView', params: { moviePk: movie.id } }">
      <img :src="getImageUrl(movie.poster_url)" class="movie-poster" alt="movieposter" />

    </RouterLink>
    </div>
 
</template>

<script setup>
import { ref } from 'vue';

defineProps({
  movie: Object,
});



// 영화 포스터 URL 생성 함수
const getImageUrl = (path) => {
  if (!path) {
    return;
  }
  return `https://image.tmdb.org/t/p/w500${path}`;
};
</script>

<style scoped>
.card {
  width: 100%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
  background-color: white;
  display: flex;
  flex-direction: column;
}

.movie-poster {
  width: 100%;
  height: auto;
}

.card-body {
  padding: 8px;
}

.card-title {
  font-size: 1rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}


</style>
