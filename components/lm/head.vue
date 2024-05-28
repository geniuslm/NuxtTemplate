<script setup lang="ts">

</script>

<template>
  <div class="flex items-center justify-between rounded bg-gray-900 w-full p-4 gap-1.5">
    <UIcon class="text-primary-500 w-7 h-7"  name="i-heroicons-shopping-bag-solid"/>

    <div class="text-2xl text-neutral-300 font-semibold ">李默眼镜工作室</div>
    <div class="flex-grow"></div>
    <ColorScheme>
      <USelect v-model="$colorMode.preference" :options="['system', 'light', 'dark', 'sepia']"/>
    </ColorScheme>
  </div>
</template>

<style>
/* 考虑到样式的需求，您可以在这里添加一些全局或组件特定的样式 */
</style>


<style scoped>

</style>