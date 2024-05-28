<template>
  <div class="flex flex-col h-screen bg-gray-500 gap-1 p-1">
    <!-- 顶部导航：使用固定高度和背景色，以确保与页脚一致性 -->
    <header class="flex  h-14 ">
      <LmHead/>
    </header>

    <!-- 主体内容：利用 flex-1 让主体内容填充剩余空间，并允许内容溢出时滚动 -->
    <div class="flex-1 flex overflow-auto  gap-1">
      <!-- 动态控制的侧边导航：确保高度充满父容器，如果内部内容超出，也应处理滚动 -->
      <lm-side class="h-full overflow-y-auto"/>

      <!-- 页面内容：flex-1 使其填充除侧边导航外的剩余空间，overflow-auto 处理溢出内容 -->
      <NuxtPage class="flex-1 overflow-y-auto"/>
    </div>

    <!-- 页脚：使用与顶部导航相同的高度和背景色，保持视觉一致性 -->
    <footer class="h-14  ">
      <LmFoot/>
    </footer>
  </div>
</template>

<style>
/* 考虑到样式的需求，您可以在这里添加一些全局或组件特定的样式 */
</style>


<script setup lang="ts">
import {ref} from 'vue';

// 定义一个响应式引用，用于控制侧边导航的宽度
const asideWidth = ref('w-10'); // 默认宽度为w-64 (即tailwindcss中定义的宽度为16rem)

// 当鼠标进入时执行的方法
function expandAside() {
  asideWidth.value = 'w-48';
}

// 当鼠标离开时执行的方法
function shrinkAside() {
  asideWidth.value = 'w-10';
}
</script>
