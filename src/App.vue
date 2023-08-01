<script setup>
import { useMyinfoStore } from '@/stores/myinfo'
const myinfoStore = useMyinfoStore()

import { useConfigStore } from '@/stores/config'
const configStore = useConfigStore()

import { useMyinfoAPI } from '@/apis/myinfo'
const { getMyinfoAPI } = useMyinfoAPI(configStore.backendURL)

import { useConfigAPI } from './apis/config'
const { refreshCookiesAPI } = useConfigAPI(configStore.backendURL)

async function refreshCookies(){
    const res = await refreshCookiesAPI()
    configStore.cookiesJSON = JSON.stringify(res)
}

async function getMyinfo(){
    const res = await getMyinfoAPI()
    if (res.code === 0){
        myinfoStore.myinfoObj = res.data
        myinfoStore.logged = true
    }
    else{
        myinfoStore.myinfoObj = {}
        myinfoStore.logged = false
    }
}

refreshCookies().then(() => getMyinfo())
</script>

<template>
<RouterView/>
</template>

<style lang='scss'>
@import './styles/colors.scss';

body {
    margin: 0 0;
    width: 100vw;
    height: 100vh;
}
</style>
