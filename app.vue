<template>
  <div class="flex flex-col min-h-screen">
    <!-- 顶部导航 -->
    <header class="bg-gray-700 text-white">
      <LmHead/>
    </header>

    <!-- 主体内容 -->
    <div class="flex flex-1">
      <!-- 动态控制的侧边导航 -->
      <lm-side/>

      <!-- 页面内容 -->
      <main class="flex-1">
        <NuxtPage/>
      </main>
    </div>

    <!-- 页脚 -->
    <footer class="bg-gray-700 text-white">
      <LmFoot/>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

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
