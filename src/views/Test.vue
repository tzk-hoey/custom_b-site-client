<template>
    <PictureGroup />
</template>

<script setup>
import { defineStore } from 'pinia'
import { ref } from 'vue'

const useStore = defineStore(
    'foo',
    () => {
        const bar = ref('')
        return {
            bar
        }
    }
)
const store = useStore()
const bar = store.bar
</script>