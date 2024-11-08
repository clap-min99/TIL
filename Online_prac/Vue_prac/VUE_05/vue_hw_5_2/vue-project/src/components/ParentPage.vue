<template>
    <div>
        <h1>부모 페이지 입니다.</h1>
        <ChildPage 
        v-for="child in children"
        :key="child.id"
        :my-prop="child"
        />
    </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue';
let id = 0

const children = ref([
    {id: id++, name: '김하나', age:30 },
    {id: id++, name: '김두리', age:20 },
    {id: id++, name: '김서이', age:10 },

])

</script>

<style scoped>

</style>