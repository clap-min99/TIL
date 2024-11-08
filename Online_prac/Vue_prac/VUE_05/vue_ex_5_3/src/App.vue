<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <!-- ProductList에 products 넘겨주고, add-to-cart 넘겨주기 -->
    <ProductList :products="products" @add-to-cart="addToCart"/>
    <p>총 가격: {{ totalPrice }}원</p>
    <Cart :cart="cart" @remove-product="removeProduct"/>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from './components/Cart.vue';
let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const cart = ref([])

const addToCart = function (product) {
  cart.value.push(product)
}

const removeProduct = function (product) {
  const index = cart.value.findIndex(item => item.id === product.id)
  if (index !== -1) {
    cart.value.splice(index, 1)
  }
}

const totalPrice = computed (() => {
  let sumPrice = 0
  cart.value.forEach(item => {
    sumPrice += item.price
  })
  return sumPrice
})

</script>
