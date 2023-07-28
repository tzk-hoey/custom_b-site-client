<template>
<div class="card-wrapper">
    <el-card class="card-body" :body-style="{ padding: '0px' }">
        <div class="card-floating">{{ data.floating }}</div>
        <div class="card-floating bottom">{{ data.floatingBottom }}</div>
        <img v-lazy-img="data.picture" :alt="data.title" src="" @click="imgClickHandler">
        <div class="text-area">
            <div class="card-title" :title="data.title">{{data.title}}</div>
            <div class="card-subtitle">{{data.subtitle}}</div>
        </div>
    </el-card>
</div>

</template>

<script setup>
const props = defineProps({
    data: {
        type: Object,
        default: {}
    }
})

function imgClickHandler(){
    if (props.data.url){
        window.open(props.data.url)
    }
}
</script>

<style scoped lang="scss">

.card-body{
    width: 300px;
    
    height: auto;

    img{
        width: 100%;
        height: 200px;
        object-fit: fill;

        &:hover{
            cursor: pointer;
        }
    }

    .card-title{
        width: 100%;
        height: 32px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .card-subtitle{
        height: 32px;
        width: 100%;
    }

    .card-floating{
        background-color: black;
        color: white;
        opacity: 70%;
        position: absolute;
        margin: 2px 2px;

        
    }

    .card-floating.bottom{
        margin: 178px 2px;
    }

    &:hover{
        .text-area{
            background-color: var(--el-color-primary-light-8);
        }
    }
}
</style>