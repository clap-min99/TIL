<template>
    <div>
        {{ myMsg }}
        <ParentGrandChild 
        :my-msg="myMsg"/>
        <p>{{ dynamicProps }}</p>
        <button @click="$emit('someEvent')">클릭</button>
        <button @click="buttonClick">클릭</button>
    </div>
  </template>   
  
  <script setup>
  import ParentGrandChild from './ParentGrandChild.vue';

  defineProps({
    myMsg: String,
    dynamicProps: String,
  })
  
  const emit = defineEmits(['someEvent'])
  
  const buttonClick = function ()
 {
    emit('someEvent')
 }  
  
  </script>
  
  <style scoped>
  
  </style>