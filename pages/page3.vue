<script setup lang="ts">
let numBlocks = ref(30)
</script>

<template>
  <div class="flex flex-col h-full w-full bg-gray-900 rounded p-2 gap-2">
    <!-- 固定高度的顶部部分 -->
    <div class="flex flex-col space-y-2">
      <div class="flex  p-2 gap-2">
        <UButton>page3</UButton>
        <UButtonGroup size="sm" orientation="horizontal">
          <UInput/>
          <UButton icon="i-heroicons-magnifying-glass-solid" color="gray"/>
        </UButtonGroup>
        <UButtonGroup size="xs" orientation="horizontal">
          <UButton label="王八" color="white"/>
          <UButton icon="i-heroicons-user-plus-16-solid" color="gray"/>
        </UButtonGroup>
      </div>
      <div class="flex  flex-col gap-2">
        <UButton class="w-2/6">page3</UButton>
        <UButtonGroup size="sm" orientation="horizontal">
          <UInput/>
          <UButton icon="i-heroicons-clipboard-document" color="gray"/>
          <UButton icon="i-heroicons-user-plus-16-solid" color="gray"/>
          <UButton icon="i-heroicons-magnifying-glass-solid" color="gray"/>
        </UButtonGroup>
      </div>
    </div>

    <!-- 可滚动的内容区域 -->
    <div class="flex flex-col flex-1 overflow-hidden">
      <UButtonGroup size="sm" orientation="horizontal">
        <UInput/>
        <UButton icon="i-heroicons-clipboard-document" color="gray"/>
        <UButton icon="i-heroicons-user-plus-16-solid" color="gray"/>
        <UButton icon="i-heroicons-magnifying-glass-solid" color="gray"/>
        <UButton icon="i-heroicons-clipboard-document" color="gray"/>
        <UButton icon="i-heroicons-user-plus-16-solid" color="gray"/>
        <UButton icon="i-heroicons-magnifying-glass-solid" color="gray"/>
      </UButtonGroup>
      <div class="flex-1 overflow-y-auto bg-amber-600 gap-2 p-4">
        <div v-for="n in numBlocks" :key="n" class="min-h-16 bg-primary-900 rounded-lg mb-2"></div>
      </div>
    </div>
  </div>
</template>



<style scoped>

</style>