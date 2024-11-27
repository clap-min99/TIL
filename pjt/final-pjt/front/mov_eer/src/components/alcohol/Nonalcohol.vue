<template>
  <div>
    <div v-if="nonAlcohols.length" class="subtypes-container">
      <!-- 각 논알콜 유형에 대한 카드! -->
      <RouterLink
        v-for="nonAlcohol in nonAlcohols"
        :key="nonAlcohol.subtype"
        :to="`/${nonAlcohol.subtype.toLowerCase()}`"
        class="subtype-card"
      >
        <h4>{{ nonAlcohol.subtype }}</h4>
        <div class="nonalcohol-image-container">
          <img
            v-if="nonAlcohol.images.length"
            :src="`http://127.0.0.1:8000${nonAlcohol.images[0].image}`"
            :alt="nonAlcohol.images[0].description"
            class="nonalcohol-image"
          />
        </div>
      </RouterLink>
    </div>
    <div v-else>
      <p>Loading non-alcoholic beverages...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useLiquorStore } from "@/stores/liquor";
import { RouterLink } from "vue-router";

const store = useLiquorStore(); // 스토어 사용
const nonAlcohols = ref([]); // 논알콜 데이터를 저장할 ref

// 컴포넌트가 마운트될 때 API 호출
onMounted(() => {
  store.getNonalcohols(); // 스토어의 메서드 호출
  nonAlcohols.value = store.nonalcohols; // 스토어의 nonAlcohols를 컴포넌트 데이터로 연결
});
</script>

<style scoped>
.subtypes-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
  margin-left: 90px;
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

.nonalcohol-image-container {
  margin-top: 10px;
  
  display: flex;
  justify-content: center;
}

.nonalcohol-image {
  width: 80px;
  height: auto;
  border-radius: 4px;
  /* box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); */
}
</style>
