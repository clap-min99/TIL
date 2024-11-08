<template>
  <div class="app">
    <header class="header">
      <h1>명함 관리 페이지</h1>
    </header>
    <main class="main">
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </main>
    
    <article class="article">

    </article>
    <footer class="footer"></footer>

  </div>
</template>

<script setup>

</script>

<style scoped>
.app {
  text-align: center;
  /* display: flex; */
  align-items: center;
  justify-content: space-between;
}

.header {
  padding: 20px;
  background-color: blue;
  color: white;
}

.main {
  flex-grow: 1;
  padding: 20px
}

.article {
  padding:20px;
}

.footer {
  padding: 10px;
  background-color: white;
  width:100%;
}
</style>
