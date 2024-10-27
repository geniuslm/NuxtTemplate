<script setup lang="ts">
import { ref } from 'vue'

// 定义组件的props
const props = defineProps<{
  files: string[]
}>()

// 定义事件
const emit = defineEmits<{
  refresh: []
}>()

// 音频控制相关的状态
const currentPlayingFile = ref<string>('')
const currentAudio = ref<HTMLAudioElement | null>(null)

// 播放音频方法
const 播放音频 = (filename: string) => {
  // 如果点击的是当前正在播放的文件
  if (currentPlayingFile.value === filename && currentAudio.value) {
    if (currentAudio.value.paused) {
      currentAudio.value.play()
    } else {
      currentAudio.value.pause()
    }
    return
  }

  // 如果之前有播放的音频，停止它
  if (currentAudio.value) {
    currentAudio.value.pause()
    currentAudio.value = null
    currentPlayingFile.value = ''
  }

  // 播放新的音频
  const audio = new Audio(`http://localhost:4000/audio/stream/${filename}`)
  currentAudio.value = audio
  currentPlayingFile.value = filename

  audio.play()

  // 监听音频播放结束
  audio.onended = () => {
    currentPlayingFile.value = ''
    currentAudio.value = null
  }
}

const 下载音频 = (filename: string) => {
  window.open(`http://localhost:4000/audio/stream/${filename}`, '_blank')
}
</script>

<template>
  <div class="flex flex-col">
    <!-- 标题和刷新按钮 -->
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-xl text-white">音频文件列表</h2>
      <UButton @click="emit('refresh')">刷新列表</UButton>
    </div>

    <!-- 直接使用 overflow-y-auto，类似 page2 的方式 -->
    <div class="bg-gray-800 p-4 rounded overflow-y-auto">
      <div v-if="files.length === 0" class="text-gray-400">
        暂无音频文件
      </div>
      <div v-else class="space-y-2">
        <div v-for="file in files" :key="file" :class="[
          'text-white flex items-center justify-between p-2 rounded',
          currentPlayingFile === file ? 'bg-primary-500 bg-opacity-20' : ''
        ]">
          <span>{{ file }}</span>
          <div class="flex gap-2">
            <UButton 
              :icon="currentPlayingFile === file && currentAudio?.paused === false ? 'heroicons:pause-solid' : 'heroicons:play-solid'"
              color="primary" 
              variant="ghost" 
              @click="播放音频(file)" 
            />
            <UButton 
              icon="heroicons:arrow-down-tray-20-solid" 
              color="primary" 
              variant="ghost" 
              @click="下载音频(file)" 
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* 自定义滚动条样式 */
.scrollbar-thin::-webkit-scrollbar {
  width: 6px;
}

.scrollbar-thin::-webkit-scrollbar-track {
  background: rgb(31, 41, 55); /* gray-800 */
}

.scrollbar-thin::-webkit-scrollbar-thumb {
  background: rgb(75, 85, 99); /* gray-600 */
  border-radius: 3px;
}

.scrollbar-thin::-webkit-scrollbar-thumb:hover {
  background: rgb(107, 114, 128); /* gray-500 */
}
</style>
