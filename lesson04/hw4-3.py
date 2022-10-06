import numpy as np
grades = np.load('lesson04\my_grades.npy')
d_value = np.round(grades - grades.mean(axis=1).reshape(grades.shape[0], 1), 2)
print('读取的成绩簿为: \n', grades, end='\n\n')
print('每个同学每一门成绩和平均成绩的差值为: \n', d_value, end='\n\n')
