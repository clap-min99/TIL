<template>
  <div class="background">
    <div class="auth-container">
      <h1>회원가입</h1>
      <form @submit.prevent="signUp">
        <input 
          type="text" 
          id="username" 
          v-model.trim="username"
          placeholder="아이디를 입력해주세요"
        />
        <br />
  
        <input 
          type="password" 
          id="password1" 
          v-model.trim="password1"
          placeholder="비밀번호를 입력해주세요"
        />
        <br />
  
        <input 
          type="password" 
          id="password2" 
          v-model.trim="password2"
          placeholder="비밀번호를 확인해주세요"
        />
        <br />
        <input type="submit" value="회원가입" />
      </form>
    </div>
  </div>
</template>
  
<script setup>
import { ref } from 'vue';
import { useLogStore } from '@/stores/log';
  
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
  
const store = useLogStore();
  
const signUp = function () {
  if (password1.value !== password2.value) {
    alert('비밀번호가 일치하지 않습니다.');
    return;
  }
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
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
</style>
