import { createApp } from 'vue'
import App from './App.vue'
const app = createApp(App)

import { createPinia } from 'pinia'
import { createPersistedState } from 'pinia-persistedstate-plugin'
const pinia = createPinia()
pinia.use(createPersistedState())
app.use(pinia)

import { customComponents } from './components'
app.use(customComponents)

import { customDirectives } from './directives'
app.use(customDirectives)

import router from './router'
app.use(router)

import * as ElementPlusIconsVue from '@element-plus/icons-vue'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

import '@/styles/dark.scss'

app.mount('#app')