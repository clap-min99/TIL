<template>
  <div>
    <div v-if="whiskeys.length" class="subtypes-container">
      <!-- 각 위스키 유형에 대한 카드 -->
      <RouterLink
        v-for="whiskey in whiskeys"
        :key="whiskey.subtype"
        :to="`/${whiskey.subtype.toLowerCase()}`"
        class="subtype-card"
      >
        <h4>{{ whiskey.subtype }}</h4>
        <div class="whiskey-image-container">
          <img
            v-if="whiskey.images.length"
            :src="`http://127.0.0.1:8000${whiskey.images[0].image}`"
            :alt="whiskey.images[0].description"
            class="whiskey-image"
          />
        </div>
      </RouterLink>
    </div>
    <div v-else>
      <p>Loading whiskeys...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useLiquorStore } from "@/stores/liquor";
import { RouterLink } from "vue-router";

const store = useLiquorStore(); // 스토어 사용
const whiskeys = ref([]); // 위스키 데이터를 저장할 ref

// 컴포넌트가 마운트될 때 API 호출
onMounted(() => {
  store.getWhiskeys(); // 스토어의 메서드 호출
  whiskeys.value = store.whiskeys; // 스토어의 whiskeys를 컴포넌트 데이터로 연결
});
</script>

<style scoped>
.subtypes-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
}

.subtype-card {
  background: #dac5c5;
  background-color: rgba(187, 160, 160, 0.24);
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  width: 150px;
  cursor: pointer;
  text-decoration: none;
  color: #f8f8f7;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.subtype-card:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.subtype-card h4 {
  margin: 0;
  font-size: 1.2rem;
}

.whiskey-image-container {
  margin-top: 10px;
  display: flex;
  justify-content: center;
}

.whiskey-image {
  width: 80px;
  height: auto;
  border-radius: 4px;
  /* box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); */
}
</style>
