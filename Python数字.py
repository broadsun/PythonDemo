# -*-coding:utf-8 -*-

__author__ = "Sun Guangbo"

'''Python支持的数据类型
1、int
2、long 长整形
3、bool
4、float（双精度浮点型，等同于c语言的double）
5、十进制浮点型
6、负数
'''
aInt = 1

#Python中变量是一个指针，指向装着内容的盒子

#删除一个对象的引用
del aInt

#Python的整形等价于C语言的有符号long，Python的长整形是更大的
#目前两者已经可以悄然转化，不需要关心

aFloat = 4.3e25
aFloat = 4.2E-10

#复数
aComplex = 1+2j
aComplex.real == 1
aComplex.imag == 2

#位操作符
# ~ <<  >> & | ^
num = 2
print ~num #取反，结果为 -(num+1)
print num<<2
print num>>2

print abs(-2)     #绝对值
print round(3.17) #四舍五入
print round(3.17, 1)

import math
#floor，小于原数且最接近原数的整形
print math.floor(-3.98)
print math.floor(3.98)

#八进制，16进制与10进制的转换
#hex() 转化为16进制
#oct() 转化为8进制
#int() 转化为10进制
print hex(0377)
print oct(255)
print int(0xff)


#ASCII码与字符之间的转换
print ord('A')  #将字符转换成ASCII码
print chr(65)   #将ASCII码转换成对应字符


#bool类型是int的子类，True是1，False是0
class testbool1(object):
    pass
t1  = testbool1();
print bool(t1)

#没有__nonzero__() 方法的对象默认为True

class testbool(object):
    def __nonzero__(self):
        return False
t  = testbool();
print bool(t)


#十进制浮点型
import decimal
dec = decimal.Decimal("3.14")
'''
#相关模块
decimal
array
math
operator
random
'''
import random
print random.random() #伪随机数
import os
print os.urandom(3)    #强随机数















