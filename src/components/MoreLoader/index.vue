<template>
<div class="more-loader-bar" ref="elref">
    {{ text }}
</div>
</template>

<script setup>
import { useIntersectionObserver } from '@vueuse/core'
import { ref, onMounted } from 'vue' 

const props = defineProps({
    loader: {
        type: Function,
        default: () => false
    },
    text: {
        type: String,
        default: "已经到底啦！"
    },
    disable: {
        type: Boolean,
        default: false
    }
})

function startObeserve(elref){
    const {stop} = useIntersectionObserver(
            elref,
            ([{ isIntersecting }]) =>  {
                if (isIntersecting) {
                    if (props.disable)
                        stop()
                    else
                        props.loader()
                }
            }
        )
}

const elref = ref(null)
startObeserve(elref)

onMounted(() => {
})
</script>

<style lang="scss">
.more-loader-bar{
    width: 100%;
    text-align: center;
}
</style>