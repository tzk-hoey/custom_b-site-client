<template>
<LayoutNav/>
<el-container>
    <LayoutSide/>
    <LayoutMain/>
</el-container>
</template>

<script setup lang="js">
import LayoutMain from './components/LayoutMain.vue';
import LayoutNav from './components/LayoutNav.vue'
import LayoutSide from './components/LayoutSide.vue';

</script>

<style scoped lang="scss">
div {
    background-color: $themecolor2;
    width: 100%;
    height: 100%
}
</style>
