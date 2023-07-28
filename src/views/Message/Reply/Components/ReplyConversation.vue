<template>
<el-card>
    <template #header>
        <div class="speech">
            <span>
                <img :src="myinfoStore.logged? myinfoStore.myinfoObj.profile.face: ''" v-if="myinfoStore.logged">
            </span>
            <span class="info-content">
                <div class="info">
                    我&nbsp;&nbsp;<a :href="data.item.uri+'#reply'+data.item.source_id" target="_blank">来源</a>
                </div>
                <div class="content">
                    {{ data.item.target_reply_content? data.item.target_reply_content: data.item.title}}
                </div>
            </span>
        </div>
    </template>
    <div class="speech">
        <span>
            <img v-lazy-img="data.user.avatar">
        </span>
        <span class="info-content">
            <div class="info">
                {{ data.user.nickname }}&nbsp;于&nbsp;{{ dayjs.unix(data.reply_time).format('YY-MM-DD HH:mm:ss') }}
            </div>
            <div class="content">
                {{ data.item.source_content }}
            </div>
        </span>
    </div>
</el-card>
</template>

<script setup>
defineProps({
    data: {
        type: Object,
        default: () => {}
    }
})

import dayjs from 'dayjs'
import { useMyinfoStore } from '@/stores/myinfo'
const myinfoStore = useMyinfoStore()
</script>

<style scoped lang="scss">
.el-card{
    margin-bottom: 10px;
    margin-right: 15px;
}
.speech{
    width: 100%;
    display: flex;
    justify-content: left;
    align-items: center;

    img{
        width: 60px;
        height: 60px;
    }

    .info-content{
        margin-left: 10px;
    }

    .info{
        font-size: larger;
    }

    .content{
        margin-top: 5px;
    }
}
</style>