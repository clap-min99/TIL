<template>
    <div class="app">
      <header class="header">
        <h1>명함 관리 페이지</h1>
      </header>
      <main class="main">
        <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
      </main>
      <article class="article">
        <BusinessCard />
      </article>
      <footer class="footer">
        <p>&copy; 2023 My Business Cards</p>
      </footer>
    </div>
  </template>
  
  
  <script setup>
  import BusinessCard from './components/BusinessCard.vue';
  </script>
  
  <style>
  .app {
    text-align: center;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
  }
  
  .header {
    padding: 20px;
    background-color: #007acc;
    color: white;
  }
  
  .main {
  
    padding: 20px;
  }
  
  .article {
    flex-grow: 1;
    padding: 20px;
  }
  
  .footer {
    padding: 10px;
    background-color: #f0f0f0;
    width: 100%;
  }
  </style>
  