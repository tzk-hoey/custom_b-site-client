<template>
    <VideoCardLayout :data="dataForCards"/>
    <MoreLoader :loader="loadMore" :disable="noMore"/>
</template>

<script setup>

import { ref } from 'vue'
import { useVideoListAPI } from '@/apis/videolist'
import { useConfigStore } from '@/stores/config'
import { shortnum } from '@/utils/shortnum'

const dataForCards = ref([])
const configStore = useConfigStore()
const { getPopularAPI } = useVideoListAPI(configStore.backendURL)

async function getPopular(pn=1, ps=20){
    const res = await getPopularAPI(pn, ps)
    if (res.code !== 0)
        return true
    for (const item of res.data.list){
        const newitem = {
            floating: '👀' + shortnum(item.stat.view) + '🗯️' + shortnum(item.stat.danmaku) + '📃' + shortnum(item.stat.reply),
            floatingBottom: ((dur) => (dur/60).toFixed(0)+':'+dur%60)(item.duration),
            picture: item.pic,
            title: item.title,
            subtitle: item.owner.name + ' - ' + item.tname,
            url: item.short_link_v2
        }
        dataForCards.value.push(newitem)
    }
    return res.data.no_more
}

let page = 1
const noMore = ref(false)
function loadMore(){
    getPopular(page).then((no_more) => {
        page += 1
        noMore.value = no_more
    })
}
</script>