<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'

// 明确定义 props 的类型
interface Props {
  messages: string[]
}

const props = defineProps<Props>()

const logContainer = ref<HTMLElement | null>(null)

// 修改 watch 的位置和使用方式
watch(() => props.messages, () => {
  nextTick(() => {
    if (logContainer.value) {
      logContainer.value.scrollTop = logContainer.value.scrollHeight
    }
  })
}, { deep: true })
</script>

<template>
  <div ref="logContainer" class="bg-gray-800 p-4 rounded h-40 overflow-y-auto">
    <div v-if="messages.length === 0" class="text-gray-400">
      暂无消息
    </div>
    <div v-else v-for="(msg, index) in messages" :key="index" class="text-white py-1">
      {{ msg }}
    </div>
  </div>
</template>
