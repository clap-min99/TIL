<template>
    <div class="business-card-detail">
      <h3>이름 : {{ businessCard.name }}</h3>
      <p>직함 : {{ businessCard.title }}</p>
      <button @click="deleteCardFunc(businessCard)">명함 삭제</button>
    </div>
  </template>
  
  <script setup>
  defineProps({
    businessCard: Object
  })

  const emit = defineEmits(['deleteCardEvent'])

  const deleteCardFunc = function (targetCard) {
    emit('deleteCardEvent', targetCard)
  }

  </script>
  
  <style>
  .business-card-detail {
    width: 40%;
    margin: 20px;
    border: 1px solid #ccc;
    padding: 20px;
    background-color: #f9f9f9;
  }
  </style>
  