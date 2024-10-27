<script setup lang="ts">
// 定义音频文件和播放器的状态
interface AudioItem {
  name: string;
  file: File;
  url: string;
}

const audioList = ref<AudioItem[]>([]);
const currentAudio = ref<HTMLAudioElement | null>(null);
const currentPlaying = ref<string>('');
const isPlaying = ref(false);

// 处理文件夹选择和音频文件读取
async function handleFolderSelect() {
  try {
    const dirHandle = await (window as any).showDirectoryPicker();
    audioList.value = [];
    
    for await (const entry of dirHandle.values()) {
      if (entry.kind === 'file' && entry.name.match(/\.(mp3|wav|ogg|m4a)$/i)) {
        const file = await entry.getFile();
        const url = URL.createObjectURL(file);
        audioList.value.push({
          name: file.name,
          file: file,
          url: url
        });
      }
    }
  } catch (err) {
    console.error('选择文件夹失败:', err);
  }
}

// 音频播放控制
function playAudio(audio: AudioItem) {
  if (currentAudio.value) {
    currentAudio.value.pause();
    if (currentPlaying.value === audio.name && isPlaying.value) {
      isPlaying.value = false;
      return;
    }
  }
  
  currentAudio.value = new Audio(audio.url);
  currentAudio.value.play();
  currentPlaying.value = audio.name;
  isPlaying.value = true;
}
</script>

<template>
  <div class="flex flex-col h-auto w-full bg-gray-900 rounded p-2 gap-2">
    <!-- 选择文件夹按钮 -->
    <UButton 
      @click="handleFolderSelect" 
      class="w-full mb-4 bg-blue-600 hover:bg-blue-700"
    >
      选择音频文件夹
    </UButton>

    <!-- 音频列表 -->
    <div class="flex flex-col gap-2 overflow-y-auto max-h-[70vh]">
      <UButton
        v-for="audio in audioList"
        :key="audio.name"
        @click="playAudio(audio)"
        class="flex justify-between items-center p-4"
        :class="{
          'bg-blue-600': currentPlaying === audio.name && isPlaying,
          'bg-gray-700': currentPlaying !== audio.name
        }"
      >
        <span class="truncate">{{ audio.name }}</span>
        <span v-if="currentPlaying === audio.name && isPlaying">
          正在播放
        </span>
      </UButton>

      <!-- 空状态提示 -->
      <div 
        v-if="!audioList.length" 
        class="text-gray-400 text-center p-4"
      >
        请选择包含音频文件的文件夹
      </div>
    </div>
  </div>
</template>

<style scoped>
.truncate {
  max-width: 80%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
