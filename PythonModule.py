# -*- coding:utf-8 -*-

__author__ = 'Sun Guangbo'

#模块路径修改
import sys
print sys.path #path里面是一个路径的列表
#增加新的路径
sys.path.append("../../")

#查看导入了哪些模块，一个字典
#key是模块名称
#value是模块的路径
#print sys.modules


#内建命名空间，由 __buitlins__ 模块中的名字构成
#Python解释器首先加载  __buitlins__模块

testval = 1024
def testspace():
	localval = 2048
	print '#########LOCAL is ', locals()

testspace()
print "##########GLOBAL is ", globals()

'''
from import语句在换行时需要 反斜杠 \


from modules import aa, bb, cc,\
dd, ee, ff,gg

'''

# from  __future__  import  new_feature

#import语句实际上是调用了__import__(module , globals, locals, fromlist)函数
#globals, locals, fromlist默认值分别是 globals(), locals(), []
syc = __import__("sys")  # 注意：！！！！不是 __import__(sys)
print type(syc)

#上面等价于
import sys as syc
#重新导入模块
reload(sys) #注意：！！！！ 不是 reload("sys")

sys.modules.keys()

#阻止某个属性通过  from module import *  导入，在属性名前加下一个划线
#不过显示导入，没有影响。import module._attribute
