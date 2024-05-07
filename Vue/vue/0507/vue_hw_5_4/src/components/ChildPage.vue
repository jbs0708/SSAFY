<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ myProp.name}}</p>
    <p>나이 : {{ myProp.age}}</p>
    <p>용돈 : {{ myProp.balance}}</p>
    <button @click="giveMeAllowance">용돈 주세요.</button>
  </div>
</template>

<script setup>

const props = defineProps({
  myProp: Object
})

const emit = defineEmits(['money'])

const giveMeAllowance = function () {
  emit('money', props.myProp.id)
}
</script>

<style scoped>

</style>