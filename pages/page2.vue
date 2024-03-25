<script setup lang="ts">
const people = ['Wade Cooper', 'Arlene Mccoy', 'Devon Webb', 'Tom Cook', 'Tanya Fox', 'Hellen Schmidt', 'Caroline Schultz', 'Mason Heaney', 'Claudie Smitham', 'Emil Schaefer']

const selected = ref(people[0])
let numBlocks = ref(1)
</script>

<template>
  <div class="flex flex-col overflow-hidden rounded-3xl bg-amber-300">
    <UInputMenu class="" v-model="selected" :options="people"/>
    <input type="number" v-model="numBlocks" class="mt-2 mb-2" min="1" />


    <div class="flex flex-wrap gap-2 overflow-y-auto">
      <!-- 每个方块都是长宽相等的，并具有圆角 -->
      <div class="h-40 w-40 bg-primary-900 rounded-lg"></div>
      <div v-for="n in numBlocks" :key="n" class="h-40 w-40 bg-primary-900 rounded-lg"></div>
    </div>

  </div>
</template>

