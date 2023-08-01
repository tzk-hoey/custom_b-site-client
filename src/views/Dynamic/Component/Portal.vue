<template>
<el-scrollbar>
    <div class="filter-wrapper"> 
        <div class="filter-user" @click="$router.push(`/dynamic/${type}/`)" :class="{active: mid === ''}">
            <div class="filter-all">
                全部
            </div>
        </div>
        <div class="filter-user" v-for="item in data" :key="item.mid" :title="item.uname" @click="$router.push(`/dynamic/${type}/${item.mid}`)" :class="{active: item.mid == mid}">
            <img v-lazy-img="item.face">
        </div>
    </div>
</el-scrollbar>
</template>

<style scoped lang="scss">
.el-scrollbar{
    width: 95%;
    height: 95px;
    overflow: auto;

    .filter-wrapper{
        height: 80px;
        width: auto;
        white-space: nowrap;

        .filter-user{
            cursor: pointer;
            height: 80px;
            width: 80px;
            margin-right: 10px;
            display: inline-block;
            vertical-align:top;

            &:hover, &.active{
                border-style: solid;
                border-width: 1px;
                border-color: var(--font-color);
            }

            img{
                width: 100%;
                height: 100%;
                object-fit: fill;
            }

            .filter-all{
                background-color: var(--el-color-primary-light-9);
                width: 100%;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
            }
        }
    }   
}

</style>

<script setup>
defineProps({
    data: { type: Array, default: () => [] },
    type: { type: String, default: 'all'},
    mid: { type: String, default: ''}
})

</script>