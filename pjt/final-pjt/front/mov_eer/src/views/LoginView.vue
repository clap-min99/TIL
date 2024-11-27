<template>
  <div class="background">
    <div class="auth-container">
      <h1>MVBeer</h1>

      <form @submit.prevent="handleSubmit">
        <input 
          type="text" 
          id="username" 
          v-model.trim="username" 
          placeholder="아이디를 입력해주세요"
        />
        <br />

        <input 
          type="password" 
          id="password" 
          v-model.trim="password" 
          placeholder="비밀번호를 입력해주세요"
        />
        <br />

        <div class="form-options">
          <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
        </div>

        <input type="submit" value="로그인" />
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useLogStore } from '@/stores/log';
import { RouterLink } from 'vue-router';

const username = ref(null);
const password = ref(null);

const store = useLogStore();

const handleSubmit = () => {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style scoped>
.background {
  background-color: black;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.auth-container {
  background-color: #050505; /* 폼 배경색 */
  padding: 40px;
  border-radius: 8px;
  text-align: center;
  color: white;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

h1 {
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

input[type="text"],
input[type="password"] {
  padding: 10px;
  width: 100%;
  box-sizing: border-box;
  border-radius: 4px;
  border: 1px solid #555;
  background: #222;
  color: white;
}

input[type="submit"] {
  background-color: #ee9191;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

input[type="submit"]:hover {
  background-color: #fd6666;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  color: white;
  margin: 10px 0;
}

label {
  color: #ee9191;
}

a {
  color: #ee9191;
  text-decoration: underline;
}

a:hover {
  color: #fd6666;
}
</style>
