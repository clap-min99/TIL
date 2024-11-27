<template>
  <div>
    <!-- 댓글 섹션 -->
    <div class="comments-section">
      <h5>페어링 리뷰🍷</h5>
      <ul class="comments-list">
        <li v-for="comment in comments" :key="comment.id" class="comment">
          <p v-if="editingComment !== comment">
            <strong>{{ comment.user }}</strong>: {{ comment.content }}
          </p>
          <div v-if="editingComment === comment">
            <input type="text" v-model="newComment" class="comment-input" />
            <button @click="updateComment(comment.id)" class="comment-submit">수정 완료</button>
            <button @click="editingComment = null" class="comment-submit">취소</button>
          </div>
          <small>{{ new Date(comment.created_at).toLocaleString() }}</small>
          <button v-if="isAuthor(comment) && editingComment !== comment" @click="editComment(comment)">수정</button>
          <button v-if="isAuthor(comment)" @click="deleteComment(comment.id)">삭제</button>
        </li>

      </ul>
      <form @submit.prevent="submitComment">
        <input
          type="text"
          v-model="newComment"
          placeholder="리뷰를 작성해주세요"
          class="comment-input"
        />
        <button type="submit" class="comment-submit">리뷰 작성</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import axios from "axios";
import { useLogStore } from "@/stores/log";

const props = defineProps({
  movieId: {
    type: Number,
    required: true,
  },
});

const comments = ref([]);
const newComment = ref("");
const editingComment = ref(null);
const store = useLogStore();

console.log(store.API_URL)
// 댓글 불러오기
const fetchComments = () => {
  const url = `${store.API_URL}/api/v1/movies/${props.movieId}/comments/`;
  console.log(store.token)
  console.log("Fetching comments from:", url); // 디버깅용 콘솔 출력

  axios({
    method: 'get',
    url:  `${store.API_URL}/api/v1/movies/${props.movieId}/comments/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  }).then((response) => {
      console.log("댓글 API 응답:", response.data); // 응답 데이터 확인
      comments.value = response.data;
    })
    .catch((error) => {
      console.error("댓글 불러오기 실패:", error);
    });
};
    
    

// 댓글 작성
const submitComment = () => {
  if (newComment.value.trim() === "") {
    alert("댓글 내용을 입력하세요!");
    return;
  }

  const url = `${store.API_URL}/api/v1/movies/${props.movieId}/comments/`;
  console.log("Submitting comment to:", url); // 디버깅용 콘솔 출력

  axios
  ({
    method: 'post',
    url:  `${store.API_URL}/api/v1/movies/${props.movieId}/comments/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data:{content: newComment.value}},)
    .then((response) => {
      console.log("작성된 댓글:", response.data);
      // 댓글 추가 시 중복 방지
      if (!comments.value.some((comment) => comment.id === response.data.id)) {
        comments.value.push(response.data);
      }
      newComment.value = "";
      
    })
    .catch((error) => {
      console.error("댓글 작성 실패:", error);
    });
};

watch(() => props.movieId, (newMovieId, oldMovieId) => {
  console.log("영화 ID 변경:", oldMovieId, "->", newMovieId);
  comments.value = []; // 상태 초기화
  fetchComments(); // 새 영화 댓글 불러오기
});



const deleteComment = (commentId) => {
  if (!commentId) {
    console.error("Invalid commentId:", commentId); // 로그로 잘못된 ID 출력
    return;
  }
  console.log("Deleting comment with ID:", commentId); // 유효한 ID 확인
  const url = `${store.API_URL}/api/v1/movies/${props.movieId}/comments/${commentId}/`;
  axios({
    method: 'delete',
    url: url,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      comments.value = comments.value.filter((comment) => comment.id !== commentId);
      alert("댓글이 삭제되었습니다.");
    })
    .catch((error) => {
      console.error("댓글 삭제 실패:", error);
    });
};


// 댓글 수정
const editComment = (comment) => {
  console.log("Editing comment:", comment);
  editingComment.value = comment;
  newComment.value = comment.content;
};


const updateComment = (commentId) => {
  if (!commentId) {
    console.error("Invalid commentId:", commentId); // commentId가 없는 경우 로그 출력
    return;
  }
  console.log("Updating comment with ID:", commentId); // 유효한 commentId 확인
  const url = `${store.API_URL}/api/v1/movies/${props.movieId}/comments/${commentId}/update/`;
  console.log("Update URL:", url); // 생성된 URL 확인

  axios({
    method: 'put',
    url: url,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: { content: newComment.value },
  })
    .then((response) => {
      const index = comments.value.findIndex((c) => c.id === commentId);
      comments.value[index] = response.data;
      editingComment.value = null; // 수정 모드 종료
      newComment.value = ""; // 입력 필드 초기화
      alert("댓글 수정 성공!");
    })
    .catch((error) => {
      console.error("댓글 수정 실패:", error); // 에러 발생 시 로그 출력
    });
};


// 작성자 확인
const isAuthor = (comment) => {
  console.log('현재 사용자:', store.user?.username); // 현재 로그인한 사용자 확인
  console.log('댓글 작성자:', comment.user); // 댓글 작성자 확인
  console.log(store.user)
  return store.user?.username === comment.user;
};

// 컴포넌트 초기 로드
onMounted(() => {
  console.log("Movie ID:", props.movieId); // movieId 출력
  comments.value = []
  if (!store.token) {
    alert("로그인이 필요합니다.");
    return;
  }
  fetchComments();
});
</script>

<style scoped>
/* 댓글 스타일 */
.comments-section {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #2c2c2c; /* 어두운 배경 */
  border-radius: 8px;
  color: #f1f1f1; /* 밝은 텍스트 */
}

.comments-list {
  list-style: none;
  padding: 0;
  margin-bottom: 1rem;
}

.comment {
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.comment-input {
  width: calc(100% - 100px);
  padding: 0.5rem;
  margin-right: 10px;
  margin-bottom: 15px;
  border: 1px solid #444; /* 어두운 테두리 */
  border-radius: 4px;
  background-color: #3c3c3c; /* 어두운 입력 배경 */
  color: #f1f1f1; /* 밝은 텍스트 */
}

.comment-input::placeholder {
  color: #b1b1b1; /* 입력 필드 플레이스홀더 색상 */
}

.comment-submit {
  padding: rem 1rem;
  background-color: #444; /* 어두운 버튼 배경 */
  color: #f1f1f1; /* 밝은 버튼 텍스트 */
  border: 1px solid #555; /* 버튼 테두리 */
  border-radius: 4px;
  cursor: pointer;
}

.comment-submit:hover {
  background-color: #ee9191; /* 버튼 호버 상태 */
}

.comment p {
  color: #f1f1f1; /* 댓글 텍스트 색상 */
}

small {
  color: #a1a1a1; /* 시간 표시 텍스트 색상 */
}

button {
  background-color: #444;
  color: #f1f1f1;
  border: none;
  border-radius: 4px;
  padding: 0.2rem 0.5rem;
  cursor: pointer;
}

button:hover {
  background-color: #ee9191;
}

</style>
