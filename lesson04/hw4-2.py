import numpy as np
a = np.array([[i for i in range(j, j+6)]for j in range(0, 60, 10)])
print('矩阵: \n', a, end='\n\n')
print('红色: \n', a[0, 3:5], end='\n\n')
print('蓝色: \n', a[:, 2].reshape(6, 1), end='\n\n')
print('紫色: \n', a[2::2, ::2], end='\n\n')
print('绿色: \n', a[4:, 4:], end='\n\n')
