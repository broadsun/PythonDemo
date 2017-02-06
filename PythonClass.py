# -*- coding:utf-8 -*-

__author__ = 'Sun Guangbo'

#类属性和实例属性
#查看类的属性可以用dir()

class MyClass(object):
    myVersion = '1.1'
    def showMyVersion(self):
        print MyClass.myVersion
'''
print dir(MyClass)
print MyClass.__dict__
print vars(MyClass)
'''

# __name__ 类的名字
print MyClass.__name__ 

print type("").__name__

#__module__ 类所属的模块
print MyClass.__module__

# __dict__ 属性
#一个普通对象使用__dict__ 来保存自己的属性，你可以动态地向其中添加或删除属性
'''
1、类和类的实例都有__dict__属性，两者互不影响
2、dir()查找的顺序为 类的实例，类，类的父类
'''
#一个类有 __slots__ 属性，那么它就没有 __dict__ 属性
class testDir(object):
    #__slots__ = ['classAttr','instanceAttr']
    def __init__(self):
        self.instanceAttr = 1
    classAttr = 2

testDir.classAttr1 = 3

x = testDir()
print "dir(x) is :  ", dir(x)
print 'class __dict__ is ', testDir.__dict__
print 'instance __dict__ is :  ',x.__dict__
del testDir.classAttr1 #删除属性
print dir(x)

# __slots__ 属性，使代码更节省内存
#限制类绑定的属性，但是只对当前类起作用
#子类如果继承了当前类，只有在定义了__slots__情况下，子类的__slots__是父类的__slots__和子类__slots__的并集
#绑定不在__slots__中的属性将触发AttributeError



# __all__ 属性，用于模块导入时
# from module import *  ，如果定义了 __all__ ，那么只有 __all__ 里面的属性可以被导入














# __init__ 方法
'''
1、没有调用new，也没有定义构造器，Python为你创建了一个对象
2、__init__ 是在创建一个实例后调用的第一个方法
'''

#__new__ 方法
#http://www.cnblogs.com/ifantastic/p/3175735.html

#新式类才有的方法
class A(object):
    pass
 
class B(A):
    def __init__(self):
        print "init"
    def __new__(cls,*args, **kwargs):
        print "new %s"%cls
        return object.__new__(cls, *args, **kwargs)
 
