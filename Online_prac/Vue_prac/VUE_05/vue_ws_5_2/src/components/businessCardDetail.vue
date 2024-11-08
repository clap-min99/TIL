<template>
    <div>
        <ul class="business-card-detail">
            <p>이름: {{ businessCard.name }}</p>
            <p>직함: {{ businessCard.title }}</p>
        </ul>
    </div>
</template>

<script setup>
defineProps({
    businessCard:Object
})
</script>

<style scoped>
.business-card-detail {
  width: 40%;
  margin: 20px;
  border: 1px solid #ccc;
  padding: 20px;
  background-color: #f9f9f9;
}
</style>