import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useConfigStore = defineStore(
    'config',
    () => {
        const backendURL = ref('')
        const cookiesJSON = ref('')

        return {
            backendURL,
            cookiesJSON
        }
    },
    {
        persist: true
    }
)