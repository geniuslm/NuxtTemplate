<template >
  <div class="h-auto w-full bg-gray-900 rounded  p-2">
    <h1>颜色模式: {{ $colorMode.value }}</h1>
    <select v-model="$colorMode.preference">
      <option value="system">System</option>
      <option value="light">Light</option>
      <option value="dark">Dark</option>
      <option value="sepia">Sepia</option>
    </select>
    <H1>这页是Index</H1>
    <UButton >颜色</UButton>
  </div>
</template>

<script setup>

</script>

<style>


</style>
