<template>
  <div class="whiskey-view">
    <h1 class="view-title">Whiskey</h1>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="!whiskeys.length" class="no-data">
      No whiskeys or associated movies found.
    </div>
    <div class="movies-container">
      <div v-for="whiskey in whiskeys" :key="whiskey.id" class="whiskey-section">
        <!-- RouterLink를 사용하여 View로 이동 -->
        <h2 class="whiskey-title">
          <RouterLink class="subtype-button" :to="`/${whiskey.subtype.toLowerCase()}`">
            {{ whiskey.subtype }}
          </RouterLink>
        </h2>
        <div class="movies-scroll">
          <div
            v-for="movie in getWhiskeyMovies(whiskey.subtype)"
            :key="movie.id"
            class="movie-card"
          >
            <RouterLink :to="{ name: 'MovieDetailView', params: { moviePk: movie.id } }">
              <img :src="getImageUrl(movie.poster_url)" class="movie-poster" alt="Movie Poster" />
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useLiquorStore } from "@/stores/liquor";
import { useMovieStore } from "@/stores/movie";
import { computed, onMounted } from "vue";
import { RouterLink } from "vue-router";

const liquorStore = useLiquorStore();
const movieStore = useMovieStore();

onMounted(() => {
  liquorStore.getWhiskeys();
  movieStore.getMovies();
  movieStore.getGenres();
});

const whiskeys = computed(() => liquorStore.whiskeys);
const movies = computed(() => movieStore.movies);
const genres = computed(() => movieStore.genres);
const loading = computed(() => !liquorStore.whiskeys.length || !movieStore.movies.length);

const getWhiskeyMovies = (subtype) => {
  return movies.value.filter((movie) => {
    return movie.genres.some((genreId) => {
      const genre = genres.value.find((g) => g.id === genreId);
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

.whiskey-view {
  padding: 20px;
  font-family: "Arial", sans-serif;
  background-color: rgb(22, 22, 22);
}

.view-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 20px;
  color: #ccb4b4;
}

.loading,
.no-data {
  text-align: center;
  font-size: 1.5rem;
  color: #666;
}

.whiskey-section {
  margin-bottom: 40px;
}

.whiskey-title {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 20px;
  color: #fcfbf7;
}

.movies-scroll {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-bottom: 10px;
}

.movies-scroll::-webkit-scrollbar {
  height: 8px;
}

.movies-scroll::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

.movies-scroll::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.movie-card {
  flex: 0 0 auto;
  width: 150px;
  text-align: center;
}

.movie-poster {
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s;
}

.movie-poster:hover {
  transform: scale(1.05);
}

.movie-title {
  font-size: 1rem;
  margin-top: 10px;
  color: #f7f5f5;
  font-weight: bold;
}

/* 서브타입 버튼 */
.subtype-button {
  display: inline-block;
  padding: 10px 20px;
  margin-bottom: 10px;
  text-align: center;
  color: #f5f5f5;
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, background-color 0.3s;
}

.subtype-button:hover {
  transform: scale(1.05);
  background-color: #ee9191;
  color: #fff;
}
</style>
