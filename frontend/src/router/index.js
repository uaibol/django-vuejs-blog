import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import About from '@/views/About.vue'
import Details from '@/views/Details.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/post/:id',
    name: 'PostDetails',
    component: Details,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(),
  //history: createWebHashHistory(),
  routes
})

export default router