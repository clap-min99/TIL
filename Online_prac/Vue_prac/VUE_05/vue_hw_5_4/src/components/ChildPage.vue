<template>
    <div>
        <h3>자식 페이지 입니다.</h3>
        <p>이름: {{ myProp.name }}</p>
        <p>나이: {{ myProp.age }}</p>
        <p>용돈: {{ myProp.balance }}</p>
        <button @click="giveMeAllowance">용돈 더 주세용</button>
    </div>
</template>

<script setup>

defineProps({
    myProp: Object,
})

const emit = defineEmits(['updateBalance'])

const giveMeAllowance = function()
 {
    emit('updateBalance')
 }
</script>

<style scoped>

</style>