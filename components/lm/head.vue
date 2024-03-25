<script setup lang="ts">

</script>

<template>
  <div class="">
    <h1>这里是头</h1>
    <ColorScheme><USelect v-model="$colorMode.preference" :options="['system', 'light', 'dark','sepia']" /></ColorScheme>
  </div>
</template>

<style scoped>

</style>