import os

def 获取目录结构(根目录, 排除列表=[], 缩进前缀='', 输出列表=[]):
    目录项列表 = sorted(os.listdir(根目录), key=lambda x: (not os.path.isdir(os.path.join(根目录, x)), x))
    目录项总数 = len([目录项 for 目录项 in 目录项列表 if 目录项 not in 排除列表])
    处理过的目录项数量 = 0

    for 目录项 in 目录项列表:
        if 目录项 in 排除列表:
            continue

        处理过的目录项数量 += 1
        路径 = os.path.join(根目录, 目录项)
        是目录 = os.path.isdir(路径)
        是最后一个目录项 = 处理过的目录项数量 == 目录项总数

        前缀 = '└── ' if 是最后一个目录项 else '├── '
        子项缩进前缀 = 缩进前缀 + ('    ' if 是最后一个目录项 else '│   ')

        if 是目录:
            行内容 = f'{缩进前缀}{前缀}{目录项}\\'
            输出列表.append(行内容)
            print(行内容)
            获取目录结构(路径, 排除列表, 子项缩进前缀, 输出列表)
        else:
            行内容 = f'{缩进前缀}{前缀}{目录项}'
            输出列表.append(行内容)
            print(行内容)

排除列表 = ['.idea','.nuxt','','node_modules', '.git', '其他不需要的目录或文件', '.output', '.vscode', 'node_modules']
根目录 = os.getcwd()  # 获取当前工作目录
输出列表 = []

print(f'{根目录}\\')
输出列表.append(f'{根目录}\\')
获取目录结构(根目录, 排除列表, '', 输出列表)

# 保存到文件
输出文件路径 = os.path.join(os.path.dirname(__file__), '项目结构.txt')
with open(输出文件路径, 'w', encoding='utf-8') as f:
    f.write('\n'.join(输出列表))
