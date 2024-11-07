<template>
    <div>
    <ParentChild 
    @some-event="someCallback"
    my-msg="message"
    :dynamic-props="name"
    />

    <ParentItem 
        v-for="item in items"
        :key="item.id"
        :my-prop="item"/>

    </div>
  </template>
  
  <script setup>    

    import {ref} from 'vue'
    import ParentChild from './ParentChild.vue';
    import ParentItem from './ParentItem.vue';
  
    const name = ref('람쥐다')

    const items = ref([
        {id: 1, name: '사과'},
        {id: 2, name: '바나나'},
        {id: 3, name: '딸기'}
    ])

    const someCallback = function() {
        console.log('ParentChild가 발신한 이벤트를 수신했어요!')
    }
    

  </script>
  
  <style scoped>
  
  </style>