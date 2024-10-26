<script lang="ts" setup>
// 定义表格的列
const columns = [{
  key: 'id',
  label: '序号',
  sortable: true // 是否可排序
}, {
  key: 'title',
  label: '标题',
  sortable: true // 是否可排序
}, {
  key: 'completed',
  label: '状态',
  sortable: true // 是否可排序
}, {
  key: 'actions',
  label: '操作',
  sortable: false // 是否可排序
}]

// 用 ref 函数创建响应式的 selectedColumns
const selectedColumns = ref(columns)

// 通过 computed 函数创建一个响应式的 columnsTable
const columnsTable = computed(() => columns.filter((column) => selectedColumns.value.includes(column)))

// 定义选中的行
const selectedRows = ref([])

// 定义选择行的函数
function select (row): void {
  // 找到选中行的索引
  const index = selectedRows.value.findIndex((item) => item.id === row.id)
  // 如果未找到，则添加到选中行数组
  if (index === -1) {
    selectedRows.value.push(row)
  } else {
    // 如果已存在，则从选中行数组中移除
    selectedRows.value.splice(index, 1)
  }
}

// 定义操作按钮
const actions = [
  [{
    key: 'completed',
    label: '已完成',
    icon: 'i-heroicons-check' // 对应图标
  }], [{
    key: 'uncompleted',
    label: '进行中',
    icon: 'i-heroicons-arrow-path' // 对应图标
  }]
]

// 定义筛选条件
const todoStatus = [{
  key: 'uncompleted',
  label: '进行中',
  value: false // 未完成的状态值
}, {
  key: 'completed',
  label: '已完成',
  value: true // 已完成的状态值
}]

// 定义搜索关键字
const search = ref('')
// 定义选中的状态
const selectedStatus = ref([])

// 计算搜索状态
const searchStatus = computed(() => {
  if (selectedStatus.value?.length === 0) {
    return ''
  }

  if (selectedStatus?.value?.length > 1) {
    return `?completed=${selectedStatus.value[0].value}&completed=${selectedStatus.value[1].value}`
  }

  return `?completed=${selectedStatus.value[0].value}`
})

// 重置筛选条件
const resetFilters = () => {
  search.value = ''
  selectedStatus.value = []
}

// 分页设置
const sort = ref({ column: 'id', direction: 'asc' as const })
const page = ref(1)
const pageCount = ref(10)
const pageTotal = ref(200) // 总页数，这个值应该从API动态获取
const pageFrom = computed(() => (page.value - 1) * pageCount.value + 1)
const pageTo = computed(() => Math.min(page.value * pageCount.value, pageTotal.value))

// 获取数据
const { data: todos, pending } = await useLazyAsyncData<{
  id: number
  title: string
  completed: string
}[]>('todos', () => ($fetch as any)(`https://jsonplaceholder.typicode.com/todos${searchStatus.value}`, {
  query: {
    q: search.value, // 搜索关键字
    '_page': page.value, // 当前页数
    '_limit': pageCount.value, // 每页显示的行数
    '_sort': sort.value.column, // 排序列
    '_order': sort.value.direction // 排序方向
  }
}), {
  default: () => [], // 默认值
  watch: [page, search, searchStatus, pageCount, sort] // 监听这些变量变化
})
</script>

<template>
  <UCard
      class="w-full"
      :ui="{
      base: '',
      ring: '',
      divide: 'divide-y divide-gray-200 dark:divide-gray-700',
      header: { padding: 'px-4 py-5' },
      body: { padding: '', base: 'divide-y divide-gray-200 dark:divide-gray-700' },
      footer: { padding: 'p-4' }
    }"
  >
    <template #header>
      <h2 class="font-semibold text-xl text-gray-900 dark:text-white leading-tight">
        表格
      </h2>
    </template>


    <!-- 表格 -->
    <UTable
        v-model="selectedRows"
        v-model:sort="sort"
        :rows="todos"
        :columns="columnsTable"
        :loading="pending"
        sort-asc-icon="i-heroicons-arrow-up"
        sort-desc-icon="i-heroicons-arrow-down"
        sort-mode="manual"
        class="w-full"
        :ui="{ td: { base: 'max-w-[0] truncate' }, default: { checkbox: { color: 'gray' } } }"
        @select="select"
    >
      <template #completed-data="{ row }">
        <UBadge size="xs" :label="row.completed ? '已完成' : '进行中'" :color="row.completed ? 'emerald' : 'orange'" variant="subtle" />
      </template>

      <template #actions-data="{ row }">
        <UButton
            v-if="!row.completed"
            icon="i-heroicons-check"
            size="2xs"
            color="emerald"
            variant="outline"
            :ui="{ rounded: 'rounded-full' }"
            square
        />

        <UButton
            v-else
            icon="i-heroicons-arrow-path"
            size="2xs"
            color="orange"
            variant="outline"
            :ui="{ rounded: 'rounded-full' }"
            square
        />
      </template>
    </UTable>

    <!-- 显示行数及分页 -->
    <template #footer>
      <div class="flex flex-wrap justify-between items-center">
        <div>
          <span class="text-sm leading-5">
            显示从
            <span class="font-medium">{{ pageFrom }}</span>
            到
            <span class="font-medium">{{ pageTo }}</span>
            一共
            <span class="font-medium">{{ pageTotal }}</span>
            行
          </span>
        </div>

        <UPagination
            v-model="page"
            :page-count="pageCount"
            :total="pageTotal"
            :ui="{
            wrapper: 'flex items-center gap-1',
            rounded: '!rounded-full min-w-[32px] justify-center',
            default: {
              activeButton: {
                variant: 'outline'
              }
            }
          }"
        />
      </div>
    </template>
  </UCard>
</template>