<template>
<Portal :data="portalData" v-if="dynamicType === 'all'" :type="dynamicType" :mid="dynamicMid"/>
<div class="dynamic-wrapper">
    <DynamicItem v-for="item in dynamicData" :key="item.id_str" :data="item" :is-all="dynamicType === 'all'"/>
</div>
<MoreLoader :loader="() => {getDynamic(dynamicType)}" :disable="noMore"/>
</template>

<script setup>
import DynamicItem from './Component/DynamicItem.vue'
import Portal from './Component/Portal.vue'


import { ref } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'
import { useConfigStore } from '@/stores/config'
const configStore = useConfigStore()
import { useDynamicAPI } from '@/apis/dynamic'
const { getDynamicAPI, getPortalAPI } = useDynamicAPI(configStore.backendURL)

const route = useRoute()
const dynamicType = ref(route.params.type)
const dynamicMid = ref(route.params.mid)
onBeforeRouteUpdate((to) => {
    dynamicType.value = to.params.type
    dynamicMid.value = to.params.mid
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
    const res = await getDynamicAPI(dynamicCursor.page, dynamicCursor.offset, dynamicType, dynamicMid.value)
    for (const item of res.data.items){
        dynamicData.value.push(item)
    }
    noMore.value = !res.data.has_more
    dynamicCursor.offset = res.data.offset
    dynamicCursor.page += 1
}

const portalData = ref([])
async function getPortal(){
    const res = await getPortalAPI()
    for (const item of res.data.up_list){
        portalData.value.push(item)
    }
}
getPortal()

</script>

<style scoped lang="scss">
.dynamic-wrapper{
    display: flex;
    flex-wrap: wrap;
}
</style>