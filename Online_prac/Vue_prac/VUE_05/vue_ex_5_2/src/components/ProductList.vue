<template>

    <ul>
      <ProductListitem 
    v-for="product in products" 
    :key="product.id"
    :product="product"/>
    </ul>

</template>

<script setup>

import ProductListitem from './ProductListitem.vue';
defineProps({
  products: Array
})


</script>
