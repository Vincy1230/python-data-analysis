#!/usr/bin/env python
# coding: utf-8

# <font face="微软雅黑" size=5 color=#A52A2A > Lesson 3 文件读取

# # 路径和文件管理

# + 内置的 pathlib.Path 对象
# + 内置的 os.path 对象
# + 环境管理器 open
# + glob

# ### 操作路径: 推荐 pathlib.Path 
# 官方文档：https://docs.python.org/3/library/pathlib.html#basic-use

# In[1]:


# 创建一个指向当前路径的Path对象
from pathlib import Path
root = Path(".") # “.”意味着：当前代码存在于的文件夹
root


# In[2]:


# Listing subdirectories:
[x for x in root.iterdir() if x.is_dir()]


# In[3]:


#p = Path('E:/WPy64-3902/notebooks/hyt_class/L03_documents')
p = Path('./L03_documents')
p   # p是一个路径对象，可以用路径对象的方法去操作；不是字符串。


# In[4]:


# 将路径对象转化为字符串
str(p)   #输出文件夹名字的字符串


# In[29]:


[x for x in p.iterdir() if x.is_dir()]


# In[5]:


# 查看当前工作目录
Path.cwd()


# pathlib 支持用 / 拼接路径。

# In[13]:


# 创建和删除文件夹
t = "new_folder1"
new_dir = root / t
#new_dir.mkdir("new_folder1")
new_dir.mkdir(10)
new_dir


# In[15]:


Path(new_dir).mkdir()


# In[16]:


new_dir.rmdir()


# In[9]:


get_ipython().run_line_magic('pinfo2', 'new_dir.mkdir')


# 小练习：
# + 创建一串文件夹，命名为folder0~~folder9
# + 把这些文件夹批量删掉

# In[29]:


# 练习答案
for i in range (10):    
    t = "folder" + str(i)
    new_dir = root / t 
    #new_dir.mkdir(0)
    new_dir.rmdir()


# In[17]:


i = 1
str(i)


# In[75]:


# 检查文件或文件夹是否存在
path_to_new_folder = root / "new_folder"
path_to_new_folder.exists()


# ### os模块
# 官方文档： https://docs.python.org/3/library/os.path.html

# In[36]:


import os
os.mkdir("bbb")


# In[39]:


os.rmdir('aaa')


# ### 绝对路径和相对路径

# In[18]:


#默认相对路径
f = open("summer.txt", "w")
f.write("I wanna go back to campus.")
f.close()


# In[20]:


path_summer = Path("summer.txt")
path_summer


# In[21]:


# 获取绝对路径
path_summer.absolute()


# In[82]:


path_to_new_folder.absolute()


# ###  `open` 环境管理器的使用方法
# + 文件打开和写入
# + 文件内容读取

# In[22]:


# 我们将向在当前文件夹中的名为“summer.txt”的文件写入数据

with open(path_summer, mode="w") as f:
    # 这里的缩进表示我们进入了打开文件的“环境”（context）中。
    # 离开这个缩进的空间将退出打开文件的环境，迫使该文件被关闭。
    # 就算我们在缩进中的代码导致错误，文件也将被关闭
    f.write('this is a line.\nThis is a second line.\nThis is the third line.\n')

# 文件再次被关闭。
# w表示写入文件内容，原内容被覆盖。


# In[23]:


# 操作path
with path_summer.open(mode="a") as f:
    f.write('1 this is a line.\n2 This is a second line.\n3 This is the third line.\n')


# ##### 常见打开模式

# ![open.png](attachment:7b0fb9a7-72f1-45ea-9c55-0ae043f8f5e0.png)

# In[24]:


# 演示文件对象的 `read` 方法
# 打开文件要注意选用 mode = ‘r’ 容易出现编码错误，应该清楚编码
with open(path_summer, mode="r") as f:
    # 将文件的全部内容读取为字符串
    content = f.read()
content


# In[25]:


print(content)


# 小练习：
# + 创建一个data_L03的文件夹
# + 创建一系列名为poem0~poem9的txt文件，都放在data_L03文件夹里
# + 在尾号数字为奇数的文件里面写 文件序号+ This is a poem. 
# + 在尾号数字为偶数的文件里面写 文件序号+Empty.

# In[26]:


# 练习答案
new_dir = root / 'data_L03'
Path(new_dir).mkdir()

for i in range (20):    
    t = "poem" + str(i) + '.txt'
    path_to_poem = root / 'data_L03'/ t
    with path_to_poem.open(mode="w") as f:
        f.write('%d This is a poem.\n' % i)


# ###  glob  查找符合条件的文件

# In[27]:


# 使用“glob”来返回所有符合某规律的文件的生成器

py_list = list((root).glob("*.py"))  # 通配符 *
py_list


# In[28]:


path_to_poems = root / 'data_L03'
files = list(path_to_poems.glob('poem*.txt') ) # 这返回一个生成器
files
# 获取这些路径的排序列表
sorted(files)


# In[29]:


filenames = [str(i) for i in files]
sorted(filenames, key = lambda x: int((x.split(".")[0].split('m')[1])))


# In[30]:


# 直接迭代这个生成器
for file in path_to_poems.glob('poem*.txt'):
    with open(file, 'r') as f:
    # 进行一些操作
        content = f.read()    
        print(content)


# In[27]:


# 迭代文件名
filenames_new = sorted(filenames, key = lambda x: int((x.split(".")[0].split('m')[1])))
for name in filenames_new:
    filename = name.split(".")[0].split('\\')[1] + '.txt'
    file_path = root / 'data_L03' / filename
    with open(file_path, 'r') as f:
    # 进行一些操作
        content = f.read()    
        print(content)


# # 数据文件处理
# - Excel和csv文件
# - json
# - NumPy数组文件

# ### pandas 文件读写

# In[32]:


import pandas as pd
path1 = '.\L03_documents\chap05-cellphone.csv'  # 相对路径不要忘记写 .
df1 = pd.read_csv(path1)
#df1 = pd.read_csv(".\L03_documents\chap05-cellphone.csv") 
df1


# In[47]:


# 写Excel文件
path3 = '.\L03_documents\cellphone.xlsx'
df1.to_excel(path3, index = None)


# In[33]:


path2 = '.\L03_documents\chap05-cellphone.xlsx'
#df2 = pd.read_excel(path2, sheet_name = "cellphone")
df2 = pd.read_excel('.\L03_documents\chap05-cellphone.xlsx', sheet_name = "cellphone")  #sheeet_name不要抄错，注意大小写
df2


# In[53]:


# 写csv文件，注意编码
path4 = '.\L03_documents\cellphone.csv'
df1.to_csv(path4, encoding = 'utf_8_sig', index = False)


# ### json模块

# In[69]:


import json


# In[70]:


# dict
names = {
    "Alex": 2020010483,
    "Jack": 2019880789,
    "Tim": [2015050888, "Phd"],
    "Eva": [2016050999, "Master"],
}
names


# In[71]:


# 三步法
f = open("names.json", "w")
# f.write(names)
json.dump(names, f)  # 把字典对象names写入文件流f
f.close()


# In[77]:


# 从 json 文件 "JSON_sample.json" 读取数据，存入变量 data
# rb 和 r 的区别：rb是为了读取二进制文件。编码和普通文件有区别。
with open("L03_documents\JSON_sample.json", 'rb') as f:
    data = json.load(f)
print(type(data))
data["0"]


# ### NumPy数组文件
# + 这是二进制文件，不是文本文件
# + NumPy用于储存数组数据的标准二进制文件类型叫做“.npy”文件。
# + NumPy用以在单个文件中储存多个数组的二进制档案格式叫做“.npz”格式。

# In[79]:


import numpy as np


# In[82]:


x = np.array([1, 2, 3])
path_to_np = root / 'L03_documents' / "my_array.npy"
# 将NumPy数组存入硬盘
np.save(path_to_np, x)


# In[84]:


# 从硬盘读取NumPy数组
y = np.load(path_to_np)
y


# In[85]:


# 将三个数组储存到NumPy档案文件中
a0 = np.array([1, 2, 3])
a1 = np.array([4, 5, 6])
a2 = np.array([7, 8, 9])

path_to_npz = root / 'L03_documents' / "my_arrays.npz"
# 我们使用关键词参数 `soil`，`crust`，和 `bedrock` 来
# 作为档案中对应数组的名字。
np.savez(path_to_npz, soil=a0, crust=a1, bedrock=a2)


# In[88]:


# 打开档案并通过名字访问每个数组
with np.load(path_to_npz) as my_archive_file:
    out0 = my_archive_file["soil"]
    out1 = my_archive_file["crust"]
    out2 = my_archive_file["bedrock"]
out0, out1, out2


# # 图像
# + matplotlib
# + OpenCV

# In[4]:


import matplotlib.pyplot as plt
path_to_boy = root / 'L03_documents' / "boy.jpg"
img = plt.imread(path_to_boy)  
plt.imshow(img)
plt.axis('off')
print(img.shape)


# In[6]:


type(img)


# In[47]:


import matplotlib.patches as patches
fig,ax = plt.subplots()
fig.set_size_inches(6,6)
im = ax.imshow(img[0:1200,:])
patch = patches.Circle((600, 600), radius = 600, transform = ax.transData)
im.set_clip_path(patch)
ax.axis('off')


# In[51]:


fig.savefig("boy.png",dpi=300,bbox_inches="tight")


# In[7]:


import cv2 as cv

img_cv = cv.imread("boy.jpg", 1) 
print(img_cv.shape)


# In[8]:


type(img_cv)


# In[27]:


# 打开一个图片文件
cv.imshow("boy", img_cv)
cv.waitKey(0)


# In[52]:


img_boy = cv.imread("boy.png") 
print(img_boy.shape)


# In[34]:


cv.imshow("boy", img_boy)
cv.waitKey(0)


# In[ ]:




