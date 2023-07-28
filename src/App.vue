<script setup>
import { useMyinfoStore } from '@/stores/myinfo'
const myinfoStore = useMyinfoStore()

import { useConfigStore } from '@/stores/config'
const configStore = useConfigStore()

import { useMyinfoAPI } from '@/apis/myinfo'
const { getMyinfoAPI } = useMyinfoAPI(configStore.backendURL)

import { useConfigAPI } from './apis/config'
const { postCookiesAPI, refreshCookiesAPI } = useConfigAPI(configStore.backendURL)

async function postCookies(){
    if (configStore.cookiesJSON){
        await postCookiesAPI(configStore.cookiesJSON)
        await refreshCookiesAPI()
    }
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


if (configStore.cookiesJSON && !myinfoStore.logged)
    postCookies().then(() => getMyinfo())
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
