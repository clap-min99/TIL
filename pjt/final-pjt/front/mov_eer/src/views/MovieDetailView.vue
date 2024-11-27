<template>
    <div>
    <nav>
    <div v-if="movie_detail">
        <MovieDetailInfo :movie="movie_detail" />
      </div>
    </nav>   
    </div>

</template>


<script setup>
import axios from 'axios'
import { RouterView, RouterLink } from 'vue-router'
import { onMounted, ref, computed } from 'vue'
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import MovieDetailInfo from '@/components/movie/MovieDetailInfo.vue';
const store = useMovieStore()
const route = useRoute()

const movie_detail = computed(() => store.movie_detail);
onMounted(() => {
  const moviePk = route.params.moviePk; // 라우트에서 moviePk 가져오기
  store.getMovie(moviePk); // Pinia의 getMovie 함수 호출로 상세 데이터 로드
});


</script>

<style scoped>

</style>