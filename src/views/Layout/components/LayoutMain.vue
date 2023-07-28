<template>
<el-container>
    <el-header>
        <el-breadcrumb separator="/">
            <el-breadcrumb-item v-for="item in breadcrumbList" :to="{ path: item.path }">
                {{ item.meta.title }}
            </el-breadcrumb-item>
        </el-breadcrumb>
    </el-header>
    <el-main>
        <RouterView/>
    </el-main>
</el-container>
</template>

<script setup>
import { onBeforeRouteUpdate, useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'

const breadcrumbList = ref([])
const route = useRoute()

function updateBreadcrumb(route){
    breadcrumbList.value.splice(0, breadcrumbList.value.length)
    for (const item of route.matched){
        if (item.meta) {
            breadcrumbList.value.push(item)
        }
    }
}

onBeforeRouteUpdate((to) => {
    updateBreadcrumb(to)
})

onMounted(() => {
    updateBreadcrumb(route)
})
</script>

<style scoped lang="scss">

</style>