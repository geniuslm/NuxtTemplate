<template>
  <div>
    <!-- 显示当前选中的颜色 -->
    <h1>当前颜色是: {{ appConfig.ui.primary }}</h1>
    <!-- 颜色选择器 -->
    <select v-model="appConfig.ui.primary">
      <!-- 循环渲染defaultColors中的颜色作为选项 -->
      <option v-for="color in defaultColors" :key="color" :value="color">{{ color }}</option>
      <!-- 静态定义的主题颜色选项 -->
    </select>
    <!-- 颜色按钮，这里没有指定功能 -->
    <UButton>颜色</UButton>
    <UTextarea/>
    <p class="text-primary-500">这是一个段落</p>

  </div>
</template>

<script setup>
import {ref} from 'vue';


const appConfig = useAppConfig();

// 定义默认颜色列表
const defaultColors = ref(['lime', 'green', 'teal', 'red', 'orange', 'amber', 'yellow', 'cyan', 'sky', 'blue', 'indigo', 'violet']);
</script>
