import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { createPersistedState } from 'pinia-plugin-persistedstate'


export const useMovieStore = defineStore('movie', () => {

  
  const movies = ref([ ]) // 전체영화목록 
  const movie_detail = ref(null) // 단일 영화 상세
  const genres = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  // 전체 영화 목록
  const getMovies = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
    .then((res) => {
      movies.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  // 영화 상세
  const getMovie = function(moviePk) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/${moviePk}`
    })
    .then((res) => {
      movie_detail.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const getGenres = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/genres/` // 장르 데이터를 가져오는 API 엔드포인트
    })
    .then((res) => {
      genres.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
  };

  const searchMovies = function(query) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/search/`,
      params: { q: query }, // 검색어를 쿼리 파라미터로 전달
    })
    .then((res) => {
      // 검색 결과를 처리
      movies.value = res.data; // movies는 Vue에서 사용하는 상태 변수
    })
    .catch((err) => {
      console.error("영화 검색 실패:", err);
    });
  };
  

  return { movies, getMovies, API_URL, getMovie, movie_detail, getGenres, genres, searchMovies}
},{ persist: true })

