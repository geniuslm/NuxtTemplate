<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Socket, io } from 'socket.io-client'

// 修改 socket 初始化方式
const socket = ref<Socket | null>(null)
const messages = ref<string[]>([])
const audioFiles = ref<string[]>([])
const inputMessage = ref('')
const currentPlayingFile = ref<string>('')
const ttsInput = ref('')
const isTTSProcessing = ref(false)

// 添加音频实例的引用
const currentAudio = ref<HTMLAudioElement | null>(null)

// 在 onMounted 中初始化 socket
onMounted(() => {
  // 确保使用 HTTPS
  socket.value = io('https://zb.lmgwr.com:4400', {
    secure: true,
    rejectUnauthorized: false
  })

  if (!socket.value) return

  console.log('尝试连接Socket.IO服务器...')
  socket.value.emit('连接')

  socket.value.on('连接成功', () => {
    console.log('Socket.IO连接成功!')
    messages.value.push('已连接到服务器')
  })

  // 添加TTS结果监听
  socket.value.on('TTS_结果', (result: { success: boolean, filename?: string, error?: string }) => {
    isTTSProcessing.value = false

    if (result.success && result.filename) {
      messages.value.push('TTS生成成功！')
      获取音频文件列表() // 刷新音频列表
      ttsInput.value = '' // 清空输入
    } else {
      messages.value.push(`TTS生成失败: ${result.error}`)
    }
  })
})



// 添加TTS发送方法
const 发送TTS请求 = () => {
  if (ttsInput.value.trim() && !isTTSProcessing.value && socket.value) {
    isTTSProcessing.value = true
    socket.value.emit('TTS', ttsInput.value)
    messages.value.push('正在生成语音...')
  }
}

// 修改获取音频文件列表方法
const 获取音频文件列表 = async () => {
  try {
    // 确保使用 HTTPS
    const response = await fetch('https://zb.lmgwr.com:4400/audio/files', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    audioFiles.value = data.files
  } catch (error) {
    console.error('获取音频文件失败:', error)
    messages.value.push(`获取音频文件失败: ${error}`)
  }
}

// 修改播放音频方法中的 URL
const 播放音频 = (filename: string) => {
  // 如果点击的是当前正在播放的文件
  if (currentPlayingFile.value === filename && currentAudio.value) {
    if (currentAudio.value.paused) {
      // 如果是暂停状态，继续播放
      currentAudio.value.play()
    } else {
      // 如果正在播放，暂停
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
  const audio = new Audio(`https://zb.lmgwr.com:4400/audio/stream/${filename}`)
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
  window.open(`https://zb.lmgwr.com:4400/audio/stream/${filename}`, '_blank')
}
</script>

<template>
  <div class="flex flex-col h-full rounded-3xl bg-gray-900 p-4">
    <!-- TTS测试区域 - 固定部分 -->
    <div class="shrink-0 mb-4">
      <h2 class="text-xl text-white">TTS 测试</h2>
      <div class="flex gap-2 mt-4">
        <UInput 
          v-model="ttsInput" 
          placeholder="输入要转换的文本" 
          :disabled="isTTSProcessing" 
          @keyup.enter="发送TTS请求"
          class="flex-1"
        />
        <UButton 
          @click="发送TTS请求" 
          :loading="isTTSProcessing" 
          :disabled="isTTSProcessing || !ttsInput.trim()"
          class="shrink-0"
        >
          生成语音
        </UButton>
      </div>
      <lm-log :messages="messages" />
    </div>

    <!-- 添加标题和刷新按钮 -->
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-xl text-white">音频文件列表</h2>
      <UButton @click="获取音频文件列表">刷新列表</UButton>
    </div>
    <!-- 音频列表区域 - 填充剩余空间 -->
    <div class="flex-grow overflow-y-auto">
      <lm-list class="h-full" :files="audioFiles" />
    </div>
  </div>
</template>
