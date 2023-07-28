<script setup>
import VideoCard from '../VideoCard/index.vue'
const props = defineProps({
    data: {
        type: Array,
        default: () => []
    }
})
</script>

<template>
<div class="cards-wrapper">
    <VideoCard v-for="item in data" :key="item.id" :data="item"/>
</div>
</template>

<style scoped lang="scss">
.cards-wrapper{
    display: flex;
    justify-content: first baseline;
    flex-wrap: wrap;

    .card-wrapper{
        margin-right: 5px;
        margin-bottom: 5px;
    }
}
</style>