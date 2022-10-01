from pathlib import Path
# 创建一个 data_L03 文件夹
Path('data_L03').mkdir()
# 在其中创建 poem0.txt ~ poem19.txt
for i in range(20):
    Path(f'data_L03/poem{i}.txt').touch()
for i in range(20):
    if i % 2 == 1:
        # 在尾号为奇数的文件里写 序号 + This is a poem
        with open(f'data_L03/poem{i}.txt', 'w') as f:
            f.write(f'{i} This is a poem')
    else:
        # 在尾号为偶数的文件里写 序号 + empty
        with open(f'data_L03/poem{i}.txt', 'w') as f:
            f.write(f'{i} empty')
# 按顺序读取所有文件并显示
for i in range(20):
    with open(f'data_L03/poem{i}.txt', 'r') as f:
        print(f.read())
