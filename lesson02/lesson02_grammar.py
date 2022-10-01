#!/usr/bin/env python
# coding: utf-8

# <font face="微软雅黑" size=5 color=#A52A2A > Lesson 2 Python基础语法

# In[1]:


#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Yating Huang
"""


# # 基本对象类型

# 一切皆“对象”

# + 数字（整数，浮点数，复数）（number（integer，float-point number，complex number））<br/>
# + 布尔值（True or False）（boolean）<br/>
# + “空”值类（None） <br/>
# + 字符串 <br/>

# In[10]:


x = 0.3

# 查看 x 的类型
type(x)


# In[12]:


# 检测 x 是否是整数类（integer）
isinstance(x, int)


# # 内置数据结构

# + 列表 list
# + 元组 tuple
# + 字符串 str
# + 字典 dict
# + 集合 set

# ### list 

# In[13]:


# 数字列表

my_list = [-1, 10*2, 7-1, 1/3, 1.3e4, (1-2j)]
my_list


# In[14]:


type(my_list), len(my_list), my_list[4], type(my_list[4]), type(my_list[-1])


# 圆括号内是tuple

# In[15]:


#isinstance(my_list, (tuple, list, str))
isinstance(my_list, (tuple, str))


# In[16]:


my_list.sort()


# In[17]:


my_list[:4].sort()
my_list


# In[18]:


my_list.remove(my_list[-1])
print(my_list)
my_list.sort(reverse = True)
my_list


# In[27]:


del my_list[-1]
my_list


# In[19]:


my_list.insert(-2, -2)
my_list


# In[20]:


0 in my_list, 0 not in my_list


# In[21]:


name = ['Tom', 'Tim', 'Tod', 'Ted', 'Jim']
i = name.index('Tod')
i, name[i]


# In[23]:


L = ['Alex',
     ['math','Chinese','English'],
     [90,80,20],
     190
    ]
L


# In[27]:


L[1][2],L[2][2]


# + 注意：索引超界报错，切片超界不报错（使用最接近的合法值，可能和你的计划不同）

# In[25]:


my_list[10]


# In[26]:


my_list[:10000]


# ### tuple

# + 列表用方括号[ ],元组用圆括号( )
# + 列表可变，元组不可变
# + 用于安全考虑，需要禁止修改序列

# In[28]:


t = ("a", False, 0, 1, 10*2, 7-1, 1/3, 1.3e4, (1-2j))
t


# In[29]:


type(t)


# In[30]:


t[3]


# In[31]:


t[3] = 5
t[3]


# In[32]:


#从list创建tuple
my_t = tuple(L)
my_t


# ### str

# - 字符串的长度
# - 字符串的提取
# - 字符串的替换
# - 格式化

# In[33]:


s = "I wanna get back to school!"
s


# In[34]:


print(s)


# In[35]:


len(s)


# In[36]:


s.split(' ')


# In[37]:


s[0], s[1:4], s[2:len(s):2]


# In[ ]:


s.


# 字符串格式化 https://www.cnblogs.com/keyou1/p/11236982.html </br>
# 可以控制输出的格式, 数据类型, 左右对齐, 宽度, 小数位数...

# In[38]:


print('%2d-%02d' % (3, 1))## d代表整数，2代表这个数字占两位字符；
print('%.2f' % 3.1415926)


# In[40]:


# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
 
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
 
# 计算半周长
s = (a + b + c) / 2
 
# 计算面积
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('三角形面积为 %0.2f' % area)


# In[ ]:





# ### dict

# In[43]:


# 使用一个词典来将食物来对应价格：名字 -> 价格
items_to_prices = {"cheese": 2.53, "milk": 3.40, "frozen pizza": 8.01}

# 查看 "frozen pizza" 的价格
items_to_prices["frozen pizza"]
8.01


# In[44]:


#将学生名字对应到考试成绩中：名字 -> 成绩
d = {'Michael': [95, 90], 'Bob': [75, 80], 'Tracy': [85, 60]} #构造字典用花括号


# In[46]:


d['Bob']


# In[89]:


#想按照语文成绩排序
get_ipython().run_line_magic('pinfo', 'sorted')


# In[48]:


sorted(d.items(), key = lambda x : x[1] , reverse = 1) 


# In[49]:


sorted(d.items(), key = lambda x : x[1][1] , reverse = False) 


# In[78]:


# 创建空词典
dict(), {}


# 合法的键可以是以下类型：
# + 数字（整数，浮点数，复数）
# + 字符串
# + 元组（但元组中的成员也必须是不可变对象）
# + 布尔值
# + 冻集（frozenset）对象

# ### set

# + 使用大括号 { } 或者 set() 函数创建集合
# + 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# In[50]:


# 初始化有着各种不可变对象的集
s = {1, 3.4, "apple", False, (1, 2, 3)}
s


# In[51]:


# 错误示范
s = {1, 3.4, "apple", False, (1, 2, 3), [1, 2, 3]}
s


# In[11]:


# 使用生成器来创建set
s1 = {i**2 for i in range(5) if i != 3}
s1


# In[52]:


# 使用set为list去重
x = [1, 2, 1, 2, 1, "moo", "moo"]
set(x)


# + 试一试：集合运算，交并补

# In[53]:


s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5}


# In[54]:


s1 & s2


# In[55]:


s1 | s2


# In[56]:


s1 - s2


# # 控制流

# + 缩进很重要
# + 条件
# + 循环
# + 函数

# In[63]:


# 线性执行的程序
x = 6
y = 23
print("x + y = ", x + y)
print("x - y = ", x - y)


# + 一个或更多的空符（空格和tab）足以作为缩进。
# + 一个有缩进的区块的每一行必须使用同样的缩进级别。
# + Python缩进的标准风格是每一层使用<font face="微软雅黑" size=3 color=#A52A2A >四个空格。

# In[67]:


# for循环的主体由一层的四空格的缩进定义，而其中的if-else
# 区块有着自己的额外的四空格缩进。
for i in [1, 2, 3, 4]:
    if i == 2 or i == 4:  # 四个空格
        x = "even"        # 八个空格
    else:                 # 四个空格
        x = "odd"         # 八个空格
    print (i, x)          # 四个空格


# ### 条件

# In[68]:


score = float(input('Score: '))
if score >= 90:
    print('Super！')
elif score >= 60:
    print('Pass.')
else:
    print('Sorry')


# In[70]:


score = float(input('Score: '))
if score >= 60:
    grade = 'P'
else:
    grade = 'F'
    print(grade)


# 注意 = 和 ==的区别

# In[71]:


x = 3   # 对变量 `x` 赋值 3
x == 3  # 检查 `x` 和 3 是否有着同样的值


# In[72]:


(x < 0) is False


# In[75]:


# 问题：输出是什么
first_item = None

if []:         ##此处把空列表换成my_list会如何？
    first_item = my_list[0]
first_item


# ### 循环
# - for
# - while
# - break
# - continue

# In[76]:


for name in ['Bob','Jim','Li Lei']:
    print('send %s an email!'%name)


# In[77]:


names = ['Bob','Jim','Li Lei']
k = 0
while(1):
    name = names[k]
    print('send %s an email!'%name)
    k = k+1
    if k >=len(names):
        break


# In[78]:


for i in range(10):
    if i%2 ==0:
        continue
    else:
        print('%d is an odd number!'%i)


# + 列表生成式

# In[113]:


numbers = [x * x for x in range(10)]
numbers


# In[115]:


numbers = [x for x in range(0, 100, 9) if x % 2 == 0]
numbers


# ### 函数

# #### 自定义函数

# In[79]:


def judge_PF(score):
    if score >= 60:
        grade = 'P'
    else:
        grade = 'F'
    return grade


# In[81]:


#调用函数
print(judge_PF(50))


# In[82]:


#不需要参数时，不要忘了括号和冒号
def ok_func():
    x = 1
    return x + 2

#调用函数
ok_func()


# In[84]:


# 你可以直接描述函数返回的对象
def count_vowels(in_string):
    """ 返回 `in_string` 中元音的数量 """
    return sum(1 for char in in_string if char in "aeiouAEIOU")


# + 注意：全局变量和局部变量

# In[86]:


total = 0 # 这是一个全局变量

def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2 # total在这里是局部变量.
   print ("函数内是局部变量 : ", total)
   return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)


# In[88]:


score = 50

def judge_PF(score):
    if score >=60:
        grade = "P"
    else:
        grade = "F"
    return grade

#请问输出是什么？

print(judge_PF(78))


# 局部作用域>全局作用域>内置作用域

# #### 匿名函数：lambda表达式

# In[89]:


f = lambda score: 'P' if score >= 60 else 'F'
print(judge_PF(80))
print(f(8))


# #### 内置函数：函数名不要与内置函数重名

# In[90]:


abs(-100),min(1,2,3),min([1,2,3])


# In[91]:


int('123'),float('1.2'),str(100)


# In[93]:


def quadratic(x,a=1,b=2,c=0): ## 默认参数，必须放在最后，且是不可变对象
    res = a*x**2+b*x+c
    return res


# In[94]:


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,3,20)
y = quadratic(x)
plt.plot(x,y)


# In[95]:


# 递归调用
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


# In[96]:


fact(6)


# In[ ]:




