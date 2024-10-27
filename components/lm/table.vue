<script setup lang="ts">
import {ref} from 'vue';


// 定义一个包含人员信息的数组，每个对象包含id、name、title、email、role和状态
const people = [{
  id: 1,
  name: 'Lindsay Walton',
  title: 'Front-end Developer',
  email: 'lindsay.walton@example.com',
  role: 'Member',
  status: true  // 添加一个布尔类型的状态字段
}, {
  id: 2,
  name: 'Courtney Henry',
  title: 'Designer',
  email: 'courtney.henry@example.com',
  role: 'Admin',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 3,
  name: 'Tom Cook',
  title: 'Director of Product',
  email: 'tom.cook@example.com',
  role: 'Member',
  status: true  // 添加一个布尔类型的状态字段
}, {
  id: 4,
  name: 'Whitney Francis',
  title: 'Copywriter',
  email: 'whitney.francis@example.com',
  role: 'Admin',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 5,
  name: 'Leonard Krasner',
  title: 'Senior Designer',
  email: 'leonard.krasner@example.com',
  role: 'Owner',
  status: true  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member',
  status: false  // 添加一个布尔类型的状态字段
}];

// 定义一个ref来存储选中的人员数组
const selected = ref([people[1]]);

const startIdx = ref(0); // 起始序号
const endIdx = ref(0);   // 结束序号

// 定义一个函数，根据起始和结束序号来设置选中的人员
const setSelectedRange = () => {
  if (startIdx.value > 0 && endIdx.value >= startIdx.value && endIdx.value <= people.length) {
    selected.value = people.slice(startIdx.value - 1, endIdx.value);
  } else {
    alert('请确保输入的序号范围正确');
  }
};
</script>

<template>
  <div >显示选定的人</div>
  <div class="h-20 " v-for="person in selected" :key="person.id">{{ person.id }} - {{ person.name }}</div>

  <UButtonGroup >
    <UInput v-model="startIdx" type="number" size="sm" icon="i-heroicons-folder" placeholder="开始的序号"/>
    <UInput v-model="endIdx" type="number" size="sm" icon="i-heroicons-folder" placeholder="结束的序号"/>
    <UButton @click="setSelectedRange">确定范围</UButton>
  </UButtonGroup>
  <UCard class="flex flex-col flex-1   overflow-y-auto  ">
    <UTable class="flex flex-col flex-1" v-model="selected" :rows="people"
            :ui="{ td: { base: 'max-w-[0] truncate' }, default: { checkbox: { color: 'primary' } } }">
      <!-- 定义一个插槽，用于显示状态图标 -->
      <template #status-data="{ row }">
        <UButton
            :icon="row.status ? 'i-heroicons-check' : 'i-heroicons-x'"
            :color="row.status ? 'emerald' : 'red'"
            size="2xs"
            variant="outline"
            :ui="{ rounded: 'rounded-full' }"
            square
        />
      </template>
    </UTable>
  </UCard>
</template>

<style scoped>

.outer-div {
  max-height: 100%; /* 限制外部div的最大高度 */
  overflow-y: auto; /* 超出部分显示滚动条 */
  position: relative; /* 相对定位 */
}

.inner-table {
  max-height: 100%; /* 限制表格的最大高度为外部div的高度 */
  overflow-y: auto; /* 超出部分显示滚动条 */
}
</style>

