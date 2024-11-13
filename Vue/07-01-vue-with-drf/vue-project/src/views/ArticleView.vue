<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{name: 'CreateView'}">Create</RouterLink>

    <ArticleList />
</div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue';
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
const store = useCounterStore()

// life cycle hook을 함수 안의 인자로 넣으면 안됨
// 호출 되는 시점을 control할 수 있는 애들이 아니다
onMounted(() => {
  // mount 되기 전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getArticles()
})

</script>

<style>

</style>
