<template>
    
    <div class="singer-detail">
        <h1>가수 이름</h1>
        <img src="@/assets/singer.jpg" alt="가수 사진" class="image-size">
        <p class="singer-description">가수 소개글</p>
    </div>

</template>

<script setup>

</script>

<style scoped>
.singer-detail {
  border: 1px solid black;
  text-align: center;
  padding: 20px;
}


.image-size {
    width: 200px;
    margin-top: 10px;
}

.singer-description {
  margin-top: 20px;
}
</style>

<!-- <style>
h1 {
    color: green
}
</style> -->