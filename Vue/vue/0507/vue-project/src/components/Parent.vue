<template>
  <div>
    <ParentChild
      my-msg = "message"
      :dynamic-props = "name"
      @some-event="someCallback"
      @my-focus="someCallback2"
      @emit-args="getNumbers"
      @update-name="updateName"
    />
    <ParentItem
      v-for="item in items"
      :key="item.id"
      :my-prop="item"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ParentChild from '@/components/ParentChild.vue'
import ParentItem from '@/components/ParentItem.vue'
const name = ref('Alice')

const someCallback = function () {
  console.log('ParentChild가 발신한 이벤트를 수신함')
}

const someCallback2 = function () {
  console.log('defineEmits 방식으로 발신된 이벤트를 수신함')
}

const items = ref([
  {id: 1, name: '사과'},
  {id: 2, name: '바나나'},
  {id: 3, name: '딸기'}
])

const getNumbers = function (...args) {
  console.log(args)
  console.log(`ParentChild가 전달한 추가인자 ${args}를 수신했어요.`)
}

const updateName = function () {
  name.value = 'Bella'
}

</script>

<style scoped>

</style>