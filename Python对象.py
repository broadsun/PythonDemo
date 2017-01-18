# -*- coding:utf-8 -*-

__author__ = "Sun Guangbo"

#一切皆为对象，对象有对象属性和特性
#对象有三个特性，身份，类型，值
#每个对象有一个身份,id()可以看成获取对象的内存地址
print id('1')
#每个对象可以查看类型，type()返回值是类型，类型也是对象
print type(1)
print type(1).__name__
#类型对象的类型都是type，它是所有Python类型的根和所有Python标准类的metaclass
print type(type('1'))

#对象的布尔值为false的情况
'''
False
None
0
0.0
0L
0.0+0.0j
""
[]
()
{}
'''

#比较操作符比较的是对象的值

#对象身份的比较 is
#在Python中，整数和短小的字符，Python都会缓存这些对象，以便重复使用
a=1.0
b=1.0
print a is b
print a is not b
id(a) == id(b)

print cmp(1,2)
print type(repr(1222))
print type(str(1345))
print type("hello world")

#旧式类
class Bar:pass
print type(Bar)
#新式类
class Foo(object):pass
print type(Foo)

num = 1.2
if type(num) is type(2.1):
    print "num is float"
import types
if type(num) is types.FloatType:
    print "num is float"
#推荐instance
if isinstance(num, float):
    print "num is float"

#以存储类型分类，原子类型（整形，字符串）和容器类型（列表，元祖，字典）
#以更新类型分类，可变类型（列表，字典）和不可变类型（数字，字符串，元祖）
#以访问类型分类，直接访问，顺序访问， 映射访问

#工厂函数：看上去是一个函数，实际上是一个类，调用它时，创建了一个类的实例，int(), type(), float()







