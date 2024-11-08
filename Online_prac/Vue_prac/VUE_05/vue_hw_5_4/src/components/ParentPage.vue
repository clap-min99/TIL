<template>
    <div>
        <h1>부모 페이지 입니다.</h1>
        <ChildPage 
        v-for="child in children"
        :key="child.id"
        :my-prop="child"
        @update-balance="updateBalance(child)"
        />
    </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue';


const children = ref([
    {id: 1, name: '김하나', age:30, balance: 100000},
    {id: 2, name: '김두리', age:20, balance: 10000},
    {id: 3, name: '김서이', age:10, balance: 1000}
])

const updateBalance = function(child) {
        
        child.balance += 1000
    }
    
</script>

<style scoped>

</style>