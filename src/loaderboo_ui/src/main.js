import './assets/main.css'

import { createApp } from 'vue'
import { createMemoryHistory, createRouter } from 'vue-router'

import App from './App.vue'
import AnimeSearch from './components/anime-components/AnimeSearch.vue';
import AnimeSearchResults from './components/anime-components/AnimeSearchResults.vue';
import WelcomeMenu from './components/WelcomeMenu.vue';

const routes = [
  { path: '', component: WelcomeMenu },
  { path: '/anime-search', component: AnimeSearch },
  { path: '/anime-search/results', component: AnimeSearchResults }
]

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
})


createApp(App).use(router).mount('#app')