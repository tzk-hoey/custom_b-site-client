<template>
<ReplyConversation v-for="item in replyData" :key="item.id" :data="item" />
<MoreLoader :loader="getReply" :disable="noMore"/>
</template>

<script setup>
import ReplyConversation from './Components/ReplyConversation.vue'
import { ref } from 'vue'

import { useConfigStore } from '@/stores/config'
const configObj = useConfigStore()

import { useMessageAPI } from '@/apis/message'
const { getReplyAPI } = useMessageAPI(configObj.backendURL)

const replyCursor = {}
const replyData = ref([])
const noMore = ref(false)
async function getReply(){
    const res = await getReplyAPI(replyCursor.id, replyCursor.time)
    replyCursor.id = res.data.cursor.id
    replyCursor.time = res.data.cursor.time
    noMore.value = res.data.cursor.is_end
    for (const item of res.data.items){
        replyData.value.push(item)
    }
}

</script>

<style scoped lang="scss">

</style>