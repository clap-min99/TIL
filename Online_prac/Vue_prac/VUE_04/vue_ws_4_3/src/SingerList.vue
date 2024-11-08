<template>
    <div class="main-page">
        <h2>가수 정보 페이지에 오신 것을 환영합니다</h2>
        <p>여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요</p>
        <img src="@/assets/microphone.jpg" alt="마이크" class="microphone-image">
        <h3>가수 목록</h3>
    </div>
    <SingerDetail />
</template>

<script setup>
import SingerDetail from './components/singers/SingerDetail.vue';
</script>

<style scoped>
.main-page {
    text-align: center;
    padding: 20px;
}

.microphone-image {
    width: 200px;
    margin-top: 10px;
}
</style>
