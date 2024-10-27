<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Socket, io } from 'socket.io-client'

// 直接初始化 socket
const socket: Socket = io('http://localhost:4000')

const messages = ref<string[]>([])
const audioFiles = ref<string[]>([])
const inputMessage = ref('')

// Socket.IO 连接
onMounted(() => {
  // 连接事件
  console.log('尝试连接Socket.IO服务器...')
  socket.emit('连接')
  
  // 监听消息
  socket.on('消息', (data: string) => {
    console.log('收到服务器消息:', data)
    messages.value.push(data)
  })

  // 添加连接状态监听
  socket.on('connect', () => {
    console.log('Socket.IO连接成功!')
  })

  socket.on('connect_error', (error: any) => {
    console.error('Socket.IO连接错误:', error)
  })

  // 获取音频文件列表
  fetchAudioFiles()
})

// 发送消息方法
const sendMessage = () => {
  if (inputMessage.value.trim()) {
    console.log('发送消息:', inputMessage.value)
    socket.emit('消息', inputMessage.value)
    inputMessage.value = ''
  }
}

// 获取音频文件列表
const fetchAudioFiles = async () => {
  try {
    const response = await fetch('http://localhost:4000/audio-files')
    const data = await response.json()
    audioFiles.value = data.files
  } catch (error) {
    console.error('获取音频文件失败:', error)
  }
}

// 页面加载时获取音频文件列表
onMounted(() => {
  fetchAudioFiles()
})
</script>

<template>
  <div class="flex flex-col h-auto w-full bg-gray-900 rounded p-4 gap-4">
    <!-- Socket.IO 测试区域 -->
    <div class="space-y-4">
      <h2 class="text-xl text-white">Socket.IO 测试</h2>
      
      <!-- 消息输入和发送 -->
      <div class="flex gap-2">
        <UInput
          v-model="inputMessage"
          placeholder="输入消息"
          @keyup.enter="sendMessage"
        />
        <UButton @click="sendMessage">发送</UButton>
      </div>

      <!-- 消息列表 -->
      <div class="bg-gray-800 p-4 rounded max-h-40 overflow-y-auto">
        <div v-for="(msg, index) in messages" :key="index" class="text-white">
          {{ msg }}
        </div>
      </div>
    </div>

    <!-- 音频文件列表 -->
    <div class="space-y-4">
      <div class="flex justify-between items-center">
        <h2 class="text-xl text-white">音频文件列表</h2>
        <UButton @click="fetchAudioFiles">刷新列表</UButton>
      </div>
      
      <div class="bg-gray-800 p-4 rounded">
        <div v-if="audioFiles.length === 0" class="text-gray-400">
          暂无音频文件
        </div>
        <div v-else class="space-y-2">
          <div v-for="file in audioFiles" :key="file" class="text-white">
            {{ file }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
