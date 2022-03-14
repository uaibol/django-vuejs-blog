import { createApp } from 'vue'
import BootstrapVue3 from 'bootstrap-vue-3'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.esm.js'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

//createApp(App).use(router).mount('#app')
const app = createApp(App)
app.use(BootstrapVue3)
app.use(router)
app.mount('#app')