#!/usr/bin/env python
# coding: utf-8

# <font face="微软雅黑" size=5 color=#A52A2A > Lesson 1 认识Python

# In[2]:


print ("hello") #python中单引号和双引号没有区别


# In[2]:


print(sum(range(10)))


# In[3]:


a = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
a


# # 算数、变量和赋值

# - 变量用来存储数据，它的值可以改变。
# - 在程序中每一个变量都有一个变量名，用英文字母、数字和下划线表示。
# - 不能以数字开头

# In[4]:


2 + 3


# In[4]:


x = 2 * (2 + 3) 


# In[5]:


x


# **动态语言**的特点：
# - 不需事先声明变量的类型
# - 变量的类型可以改变

# In[6]:


x = '你好'
print(x)


# In[7]:


x = 10
x**2 + 2*x + 3


# # 彩色代码块

# In[8]:


# 演示基本的for循环
cnt = 0
for i in range(10):
    cnt += 1

# `cnt` 现在是10
cnt


# # 你可能会看到下面这样的注释

# In[9]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# # 基础数据类型

# 整数、小数、字符串、布尔值

# In[16]:



"""
使用内置的type函数查看数据类型
"""

print(type(1))
print(type(1.0) )
#complex(1-2j)
print(type(complex(1-2j)) ) #复数
print(type('a'))
print(type(True) )#布尔型 true false


# # 通过 >>> 演示输入和输出的不同格式

# In[6]:


x = 1
x + 2
# x + 3


# # 定义函数

# In[10]:


# 定义一个范例函数
def my_func(x):
    
    return x**2


# In[13]:


# 演示 `my_func`
my_func(10.)


# # 面对错误

# In[14]:


sqrt(100)


# In[15]:


import math
math.sqrt(100)


# In[16]:


from math import sqrt
sqrt(100)


# #### 思考为什么是10.0 而不是 10

# # 字符串

# In[11]:


"the cat in the hat"


# In[12]:


'the dog in the sash'


# In[16]:


'He picked up the phone, "Hello? What do you want?" ' #注：单引号中可以把双引号当成字符输出


# In[17]:


print('He picked up the phone, \n"Hello? What do you want?" ') #输出回车


# 更多转义字符
# https://docs.python.org/2.0/ref/strings.html

# In[22]:


sentence = "Who would have thought that we were robots all along?"
len(sentence) # 长度length


# - 切片 slice:查看sentence的前四个字符，最后六个字符，或者中间的字符。

# In[11]:


sentence[:4]


# In[12]:


sentence[-6:]


# In[13]:


sentence[5:22]


# + 查看是否我们的这个字符串是否包含其它的某个的字符串。

# In[4]:


"robot" in sentence


# # 看看列表 list

# In[6]:


# 数字列表

[-1, 1/3, 10*2, 7-1, 3e9]


# In[7]:


[1, 2, "a", 0.5, "apple and orange", True, None]


# In[8]:


L = ['Alex',
     ['math','Chinese','English'],
     [90,80,20],
     190
    ]
L


# In[9]:


len(L)


# In[21]:


# 列表粘连（concatenate）

[1, 2, 3] + ["a", "b", "c"]


# + 列表本质上也是一个序列
# + 序列第一个成员的索引（index）是 0 (MATLAB总是从1开始）
# + 切片（slice）可存取其中的多个项目

# In[14]:


# 列表索引 index
my_list = [10, 20, 30, 40, 50, 60]
# my_list[0]
# my_list[1]
my_list[-1]


# In[15]:


# 看一下列表里是否存在 -5
-5 in my_list


# In[16]:


# 对列表中的项目赋值来修改列表的内容

my_list[1] = -5
-5 in my_list


# In[17]:


my_list


# In[ ]:


# 列表切片 slice
my_list[:3]


# In[18]:


# 通过切片批量更改列表中的元素
my_list[:3] = "abc"
my_list


# + 注意: 不能越界

# In[19]:


#  猜猜会出现什么结果？

my_list[6] = 'moo'


# In[20]:


# 在这个列表的结尾附加（append）一个新成员

my_list.append("moo")
my_list


# In[21]:


my_list[6] 


# # 求助

# In[24]:


get_ipython().run_line_magic('pinfo2', 'sentence.count')


# In[20]:


sentence.count('w')


# In[25]:


sentence.upper()


# + 使用'Tab'键自动完成
# + 注意不要忘记对象sentence. 的 点.

# In[17]:


get_ipython().run_line_magic('pinfo2', 'sentence.replace')


# In[23]:


sentence.replace("robot", "computer")


# # 查看版本

# In[4]:


pip --version


# In[10]:


import numpy
print(numpy.__file__)
print(numpy.__version__)


# In[1]:


pip list


# # 生成LaTeX公式

# $$\int_1^2 xdx$$

# In[20]:


import this


# <font face="微软雅黑" size=5 color=#A52A2A > Python 之禅

# + 优美胜于丑陋<br/>
# + 明了胜于晦涩<br/>
# + …… <br/>
# + 间隔胜于紧凑<br/>
# + 可读性很重要<br/>
# + …… <br/>
# + 做也许好过不做 <br/>
# + 但不假思索就动手还不如不做 <br/>

# ## PEP 8 编码风格指南
# PEP 8 Style Guide for Python Code <br/>
# 中文翻译： https://blog.csdn.net/ratsniper/article/details/78954852

# In[ ]:




