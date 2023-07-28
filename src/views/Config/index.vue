<template>
<el-form label-width="120px">
    <el-form-item label="后端URL">
        <el-col :span="12">
            <el-input v-model="configStore.backendURL" />
        </el-col>
    </el-form-item>
    <el-form-item label="Cookies">
        <el-col :span="12">
            <el-input v-model="configStore.cookiesJSON" placeholder="使用Cookie Editor输出为json格式" type="textarea" resize="none" :rows="5"/>
        </el-col>
        <el-col :span="1" :offset="1">
            <el-row>
                <el-button @click="loadCookies" size="small">读取</el-button>
            </el-row>
            <el-row>
                <el-button @click="saveCookies" size="small">保存</el-button>
            </el-row>
            <el-row>
                <el-button @click="refreshCookies" size="small">刷新</el-button>
            </el-row>
        </el-col>
    </el-form-item>
</el-form>
</template>

<script setup>
import { useMyinfoStore } from '@/stores/myinfo'
const myinfoStore = useMyinfoStore()

import { useConfigStore } from '@/stores/config'
const configStore = useConfigStore()

import { useMyinfoAPI } from '@/apis/myinfo'
const { getMyinfoAPI } = useMyinfoAPI(configStore.backendURL)

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

import { useConfigAPI } from '@/apis/config'
const { getCookiesAPI, postCookiesAPI, refreshCookiesAPI } = useConfigAPI(configStore.backendURL)

async function loadCookies(){
    const res = await getCookiesAPI()
    configStore.cookiesJSON = JSON.stringify(res)
}

async function saveCookies(){
    await postCookiesAPI(configStore.cookiesJSON)
    await getMyinfo()
}

async function refreshCookies(){
    const res = await refreshCookiesAPI()
    configStore.cookiesJSON = JSON.stringify(res)
    await getMyinfo()
}
</script>

<style lang="scss" scoped>
.el-row{
    padding-bottom: 10px;
}
</style>