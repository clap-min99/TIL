<template>
    
    <li>
    {{ product.name }} - {{ product.price }}원
    <button>장바구니에 추가</button>
    </li>
    
</template>

<script setup>
    defineProps({
        product: Object
    })
</script>

<style scoped>

</style>