<template>
  <div>
    <h1>부모 페이지입니다.</h1>
    <ChildPage 
      v-for="child in children"
      :my-prop="child"
      :key="child.id"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue'

const children = ref([
  {id:1, name:'김하나', age:30},
  {id:2, name:'김두리', age:20},
  {id:3, name:'김서이', age:10}
])

</script>

<style scoped>
div {
  padding: 10px;
  margin: 10px;
  border:1px solid gray;
}
</style>