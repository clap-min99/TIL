import axios from 'axios';

// Axios 인스턴스 생성
const api = axios.create({
  baseURL: 'http://localhost:8081', // API 기본 URL
  headers: {
    'Content-Type': 'application/json', // 기본 헤더 설정
  },
});

// 요청 인터셉터
api.interceptors.request.use(
  (config) => {
    // 요청 전에 Access 토큰을 헤더에 추가
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    // 요청 오류 처리
    return Promise.reject(error);
  }
);

// 응답 인터셉터
api.interceptors.response.use(
  (response) => {
    // 성공적인 응답 처리
    return response;
  },
  (error) => {
    const originalRequest = error.config;

    // Access 토큰 만료 시 토큰 재발급 처리
    if (
      error.response &&
      error.response.status === 401 && // 인증 실패
      !originalRequest._retry // 이미 재시도 여부 확인
    ) {
      originalRequest._retry = true; // 재시도 여부 설정

      const refreshToken = localStorage.getItem('refreshToken'); // Refresh 토큰 가져오기
      if (refreshToken) {
        return axios
          .post('http://localhost:8080/auth/token', { refreshToken })
          .then((res) => {
            const newAccessToken = res.data.token; // 새 Access 토큰
            localStorage.setItem('token', newAccessToken); // 로컬 스토리지에 저장
            originalRequest.headers.Authorization = `Bearer ${newAccessToken}`; // 요청 헤더 업데이트
            return axios(originalRequest); // 원래 요청 다시 보내기
          })
          .catch((refreshError) => {
            // Refresh 토큰 실패 시 처리
            console.error('토큰 재발급 실패:', refreshError);
            localStorage.removeItem('token');
            localStorage.removeItem('refreshToken');
            window.location.href = '/login'; // 로그인 페이지로 리다이렉트
            return Promise.reject(refreshError);
          });
      }
    }

    // 그 외의 오류 처리
    return Promise.reject(error);
  }
);

export default api;
