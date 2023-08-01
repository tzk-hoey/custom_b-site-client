<template>
    <el-scrollbar style="width: 600px; height: 210px; overflow: auto;">
    <div class="image-wrapper">
      <el-image 
        v-for="(item, index) in data"
        :key="item.id+'-img-'+index"
        style="width: 200px; height: 200px"
        :src="item.src"
        :zoom-rate="1"
        :preview-src-list="srcList"
        :initial-index="index"
        fit="cover"
        loading="lazy"
          />
    </div>
  </el-scrollbar>
</template>

<script setup>
const props = defineProps({
  data: {
    type: Array,
    defualt: () => []
  }
})
const srcList = props.data.map((item) => item.src)
</script>

<style scoped>
.image-wrapper{
  height: 100px;
  width: auto;
  white-space: nowrap;
}
</style>