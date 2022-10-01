from pathlib import Path
for i in range(1, 10):
    Path(f'folder{i}').mkdir()
    print(f'文件夹 folder{i} 已创建')
print('文件夹已创建完毕')
for i in range(1, 10):
    Path(f'folder{i}').rmdir()
    print(f'文件夹 folder{i} 已删除')
print('文件夹已删除完毕')
