<template>
    <div>
        <li>{{ myProp.name }}-{{ myProp.price }}원</li>
    </div>
</template>

<script setup>
defineProps({
    myProp:Object
})
</script>

<style scoped>

</style>