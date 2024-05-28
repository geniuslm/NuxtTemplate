<script setup lang="ts">

</script>

<template>
  <div class="flex flex-col h-auto w-full bg-gray-900 rounded p-2 gap-2">
    <div class="flex w-full p-2 gap-2">
      <UButton>page3</UButton>
      <UButtonGroup size="sm" orientation="horizontal">
        <UInput/>
        <UButton icon="i-heroicons-magnifying-glass-solid" color="gray"/>
      </UButtonGroup>
      <UButtonGroup size="xs" orientation="horizontal">
        <UButton label="王八" color="white" />
        <UButton icon="i-heroicons-user-plus-16-solid" color="gray" />
      </UButtonGroup>
    </div>
    <div class="flex  flex-col  gap-2">
      <UButton  class="w-2/6">page3</UButton>

      <UButtonGroup size="sm" orientation="horizontal">
        <UInput/>
        <UButton icon="i-heroicons-clipboard-document" color="gray"/>
        <UButton icon="i-heroicons-user-plus-16-solid" color="gray" />
        <UButton icon="i-heroicons-magnifying-glass-solid" color="gray"/>
      </UButtonGroup>
    </div>

  </div>
</template>

<style scoped>

</style>