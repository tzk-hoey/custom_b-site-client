<template>
<el-card>
    <div class="approval-item">
        <span class="info-content">
            <div class="info">
                我的{{ data.item.business }}收到{{ data.counts }}个赞，最新被点赞于{{ dayjs.unix(data.like_time).format('YY-MM-DD HH:mm:ss') }}&nbsp;&nbsp;<a :href="data.item.uri + (data.item.business === '评论'? ('#reply' +  data.item.item_id): '')" target="_blank">来源</a>
            </div>
            <div class="content">
                {{ data.item.title }}
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
.approval-item{
    width: 100%;
    display: flex;
    justify-content: left;
    align-items: center;

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