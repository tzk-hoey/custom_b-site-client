<template>
<nav>
    <div class="avatar">
        <img :src="myinfoStore.logged? myinfoStore.myinfoObj.profile.face: ''" v-if="myinfoStore.logged">
        <div class="not-logged" v-else>
            未登录
        </div>
    </div>
    <div>
        {{ myinfoStore.logged? myinfoStore.myinfoObj.profile.name: ''  }}
    </div>
</nav>
</template>

<script setup>
import { useMyinfoStore } from '@/stores/myinfo'
const myinfoStore = useMyinfoStore()
</script>

<style lang="scss" scoped>
nav {
    height: 50px;
    display: flex;
    justify-content: left;
    align-items: center;

    div{
        margin-right: 5px;
    }

    .avatar{
        background-color: var(--el-color-primary-light-9);
        height: 50px;
        width: 50px;
        display: flex;
        justify-content: center;
        align-items: center;

        img{
            width: 100%;
            height: 100%;
            object-fit: fill;
        }
    }
}
</style>