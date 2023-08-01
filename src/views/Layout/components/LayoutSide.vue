<template>
    <el-aside width="auto">
        <el-menu router :default-active="this.$route.path" :collapse="isCollapse">
            <el-menu-item @click="isCollapse = !isCollapse" index="">
                <el-icon>
                    <Expand v-if="isCollapse"/>
                    <Fold v-else />
                </el-icon>
                <span>折叠</span>
            </el-menu-item>
            <el-sub-menu index="dynamic">
                <template #title>
                    <el-icon><ChatDotSquare /></el-icon>
                    <span>动态</span>
                </template>
                <el-menu-item index="/dynamic/all">
                    <el-icon><Grid /></el-icon>
                    <span>全部</span>
                </el-menu-item>
                <el-menu-item index="/dynamic/video">
                    <el-icon><VideoCamera /></el-icon>
                    <span>视频</span>
                </el-menu-item>
            </el-sub-menu>
            <el-menu-item index="/follow">
                <el-icon><List /></el-icon>
                <span>关注</span>
            </el-menu-item>
            <el-menu-item index="/hot">
                <el-icon><DataLine /></el-icon>
                <span>热门</span>
            </el-menu-item>
            <el-sub-menu index="message">
                <template #title>
                    <el-icon><MessageBox /></el-icon>
                    <span>消息</span>
                </template>
                <el-menu-item index="/reply">
                    <el-icon><ChatDotSquare /></el-icon>
                    <span>回复</span>
                </el-menu-item>
                <el-menu-item index="/approval">
                    <el-icon><Check /></el-icon>
                    <span>点赞</span>
                </el-menu-item>
            </el-sub-menu>
            <el-menu-item index="/config">
                <el-icon><Setting /></el-icon>
                <span>设置</span>
            </el-menu-item>
            <div class="dark-switch-area">
                <el-switch v-model="isDark" :active-icon="Moon" :inactive-icon="Sunny"  inline-prompt/>
            </div>
        </el-menu>
    </el-aside>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
const router = useRouter()
const isCollapse = ref(false)

import { useDark } from '@vueuse/core'
const isDark = useDark()

import { Sunny, Moon } from '@element-plus/icons-vue'
</script>

<style scoped lang="scss">
.dark-switch-area{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>