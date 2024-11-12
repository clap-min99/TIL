import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersisdstate from 'pinia-plugin-persistedstate'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()


// app.use(createPinia())
app.use(pinia)

app.mount('#app')



