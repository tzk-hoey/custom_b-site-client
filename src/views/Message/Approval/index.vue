<template>
    <ApprovalItem v-for="item in approvalData" :key="item.id" :data="item"/>
    <MoreLoader :loader="getApproval" :disable="noMore"/>
</template>

<script setup>
import ApprovalItem from './Components/ApprovalItem.vue'

import { ref } from 'vue'
import { useMessageAPI } from '@/apis/message'
import { useConfigStore } from '@/stores/config'

const configStore = useConfigStore()
const { getApprovalAPI } = useMessageAPI(configStore.backendURL)

const approvalCursor = {}
const approvalData = ref([])
const noMore = ref(false)
async function getApproval(){
    const res = await getApprovalAPI(approvalCursor.id, approvalCursor.time)
    approvalCursor.id = res.data.total.cursor.id
    approvalCursor.time = res.data.total.cursor.time
    noMore.value = res.data.total.cursor.is_end
    for (const item of res.data.total.items){
        approvalData.value.push(item)
    }


}


</script>