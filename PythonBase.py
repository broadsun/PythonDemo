#-*- coding:utf-8 -*-

__author__ = "Sun Guangbo"

'''
1、语句语法
2、变量赋值
3、内存管理
'''
#分割符 \ 
kobe = 'king'
lbj = 'king'
if (kobe == 'king') and \
(lbj == 'king'):
    print "sgb is king"

#有一些情况不需要 \ 也可以跨行
#在使用闭合操作符时，单一语句可以跨行
#如 （） 【】 {} 里面
aList = [1,2,
3,4]
print aList


#多元赋值
x, y, z = 1, "sgb", [2,3,'haha']
print x,y,z

#两个变量交换
x, y = y, x

#关键字
import keyword
print keyword.kwlist

#避免将下划线作为变量名的开始
'''
_xxx : 不能 from module import xxx 导入
__xxx : 类的私有成员
_xxx_ : 系统定义名字

'''

#在模块，类，函数声明中，第一个没有被赋值的字符串可以通过属性 obj.__doc__来访问

#如果模块被导入 ，__name__ 为模块的名字
#如果模块被直接执行，__name__ 为 __main__

#Python中，变量不需要事先声明，也不需要定义类型
#内存可以等Python解释器自己释放，也可以del主动释放
#变量在第一次赋值时自动声明，赋值且声明后才可以使用
#对象的类型和内存占用都是运行时确定的


#对象被创建并赋值给对象时，引用计数加1
x = 3.14
#被别的别名引用时，计数加1
y = x
#作为参数传递给函数时，计数加1
def foo(x):
	pass
foo(x)
#成为容器对象的另一个元素时
myList = [1, 2, x]


#当变量关联了其他对象时，原对象计数减1
#‘xyz’计数加1
x = 'xyz'
#计数继续加1，x和y都指向 "xyz"
y = x
#计数减1, x指向 123
x = 123

#主动销毁
del y

#函数结束后，计数减一
def foo(x):
    return

#对象从容器中被移除，计数减一
x = 1
myList.remove(x)

#变量本身被销毁
del myList

#对象计数为0时，将会被解释器回收
#追踪或调试过程中，回收时间会被推迟


#解释器跟踪对象引用计数
#垃圾收集器负责释放内存，检查引用计数为0或者循环引用的对象

#使用局部变量替换模块变量，可以提高运行速度
import os
ls = os.linesep