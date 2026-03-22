import './assets/main.css'

import { createApp } from 'vue'
import { createMemoryHistory, createRouter } from 'vue-router'

import App from './App.vue'
import WelcomeMenu from './components/WelcomeMenu.vue';
import AnimeSearch from './components/anime-components/AnimeSearch.vue';
import AnimeSearchResults from './components/anime-components/AnimeSearchResults.vue';
import AnimeDownload from './components/anime-components/AnimeDownload.vue';
import AnimeDownloadScreen from './components/anime-components/AnimeDownloadScreen.vue';

export function convertStatus(status){
    if (status == 1){
        return "Upcoming";
    }else if (status == 2){
        return "Ongoing";
    }else if (status == 3){
        return "Completed";
    }else{
        return "Unknown";
    }
}

export function startAnimeSearch(anime_title){
    router.push({
        path: `/anime-search/${anime_title}` 
    })
}

export function startAnimeDownload(anime_title, anime_id, episode) {
    router.push({
        path: `/anime-download/${anime_title}/${anime_id}/${episode}` 
    })
}

export function confirmAnimeEpDownload(anime_id){
    router.push({
        path: `/anime-download/${anime_id}` 
    })
}

export function inputAnimeSearch(){
    router.push({
        path: '/anime-search'
    })
}

export function goHome(){
    router.push({
        path: '/'
    })
}

const routes = [
  { path: '', component: WelcomeMenu },
  { path: '/anime-search', component: AnimeSearch },
  { path: '/anime-search/:search_term', name: 'anime-search-results', component: AnimeSearchResults },
  { path: '/anime-download/:anime_id', name: 'anime-download', component: AnimeDownload },
  { path: '/anime-download/:anime_title/:anime_id/:ep', component: AnimeDownloadScreen }
]

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
})


createApp(App).use(router).mount('#app')