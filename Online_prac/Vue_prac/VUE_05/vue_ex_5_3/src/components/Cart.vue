<template>
    <div v-if="cart.length > 0">
        <h2>장바구니</h2>
        <ul>
            <li v-for="item in cart" :key="item.id">
                {{ item.name }} - {{ item.price }}원
                <button @click="removeProduct(item)">삭제</button>
            </li>
        </ul>
    </div>
</template>

<script setup>
defineProps({
    cart: Array
})

const emit = defineEmits(['removeProduct'])

const removeProduct = function (product) {
    emit('removeProduct', product)
}


</script>

<style scoped>

</style>