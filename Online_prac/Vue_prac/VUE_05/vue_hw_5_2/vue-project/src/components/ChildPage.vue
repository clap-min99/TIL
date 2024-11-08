<template>
    <div>
        <h3>자식 페이지 입니다.</h3>
        <p>이름: {{ myProp.name }}</p>
        <p>나이: {{ myProp.age }}</p>
            
    </div>
</template>

<script setup>
defineProps({
    myProp: Object
})
</script>

<style scoped>

</style>