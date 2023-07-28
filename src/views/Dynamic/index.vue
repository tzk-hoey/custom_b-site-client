<template>
<div class="dynamic-wrapper">
    <DynamicItem v-for="item in dynamicData" :key="item.id_str" :data="item" :is-all="dynamicType === 'all'"/>
</div>
<MoreLoader :loader="() => {getDynamic(dynamicType)}" :disable="noMore"/>
</template>

<script setup>
import DynamicItem from './Component/DynamicItem.vue'

import { ref } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'
import { useConfigStore } from '@/stores/config'
const configStore = useConfigStore()
import { useDynamicAPI } from '@/apis/dynamic'
const { getDynamicAPI } = useDynamicAPI(configStore.backendURL)

let dynamicType = useRoute().params.type
onBeforeRouteUpdate((to) => {
    dynamicType = to.params.type
    dynamicData.value.splice(0, dynamicData.value.length)
    dynamicCursor.page = 1
    dynamicCursor.offset = undefined
})

const dynamicCursor = {
    page: 1,
    offset: undefined
}
const dynamicData = ref([])
const noMore = ref(false)
async function getDynamic(dynamicType){
    const res = await getDynamicAPI(dynamicCursor.page, dynamicCursor.offset, dynamicType)
    for (const item of res.data.items){
        dynamicData.value.push(item)
    }
    noMore.value = !res.data.has_more
    dynamicCursor.offset = res.data.offset
    dynamicCursor.page += 1
}

</script>

<style scoped lang="scss">
.dynamic-wrapper{
    display: flex;
    flex-wrap: wrap;
}
</style>