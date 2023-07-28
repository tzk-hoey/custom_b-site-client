import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useMyinfoStore = defineStore(
    'myinfo',
    () => {
        const myinfoObj = ref({})
        const logged = ref(false)

        return {
            myinfoObj,
            logged
        }
    },
    {
        persist: {
            storage: sessionStorage,
        }
    }
)