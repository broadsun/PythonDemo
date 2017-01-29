# -*- coding:utf-8 -*-
__author__ = 'Sun Guangbo'

file = open("README.md")
print file.tell()
file.seek(10, 1)
print file.tell()
file.seek(0,0)
print file.tell()
file.seek(0,2)
print file.tell()


#只要程序一执行，就可以访问3个标准文件
#stdin
#stdout
#stderr
#通过sys模块获取句柄
import sys


#命令行参数argv
print sys.argv
#命令参数个数argc
print "argc is %d" % len(sys.argv)

#os模块和 os.path模块
import os
print type(os.path)

#永久性存储（介于磁盘文件和RDBMS之间）
#永久存储模块可以转换并存储Python对象
#shelve模块整合了pickle合anydbm

