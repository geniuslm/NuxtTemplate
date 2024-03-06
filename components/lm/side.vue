<script setup lang="ts">
import {ref, computed} from 'vue';


// 定义一个响应式引用，用于控制侧边导航的宽度
const asideWidth = ref('w-14'); // 默认宽度为 w-10

// 当鼠标进入时执行的方法
function expandAside() {
  asideWidth.value = 'w-48'; // 展开宽度为 w-48
}

// 当鼠标离开时执行的方法
function shrinkAside() {
  asideWidth.value = 'w-14'; // 收缩回默认宽度 w-10
}

const links = [
  {
    label: '主页',
    icon: 'i-heroicons-home-20-solid', // 假设的图标，根据实际需要更换
    to: '/'
  },
  {
    label: 'Page 1',
    icon: 'i-heroicons-document-duplicate', // 假设的图标，根据实际需要更换
    to: '/page1'
  },
  {
    label: 'Page 2',
    icon: 'i-heroicons-academic-cap-20-solid',  // 假设的图标，根据实际需要更换
    to: '/page2'
  }];

// 根据 asideWidth 的值动态调整图标大小
const iconSizeClass = computed(() => asideWidth.value === 'w-48' ? 'w-5 h-5' : 'w-7 h-7');

const uiSettings = computed(() => ({
  icon: {
    base: `transition-all duration-300 ease-in-out ${iconSizeClass.value} `,
  },
  base: 'h-14',
  wrapper: 'm-1',
  // 其他 UI 设置...
}));
</script>

<template>
  <aside :class="`bg-gray-900 text-white ${asideWidth} transition-width duration-300 ease-in-out`"
         @mouseenter="expandAside" @mouseleave="shrinkAside">
    <!-- 使用 VerticalNavigation 组件 -->
    <UVerticalNavigation :links="links" :ui="uiSettings"/>
  </aside>
</template>

<style scoped>
/* 可以在这里添加一些额外的样式，如果需要 */

</style>
