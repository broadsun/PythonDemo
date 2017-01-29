# -*- coding:utf-8 -*-

__author__ = 'Sun Guangbo'


score = 89

if score >= 90:
	print "excellect"
elif score >= 80:
	print 'good'
elif score >= 70:
	print 'average'
elif score >= 60:
	print 'pass'
else:
	print 'bad!!!'



#三元表达式

x, y  = 3,4
z = 0
if x < y:
	z = x
else:
	z = y
print z

#上面的if-else等价于下面的一行代码
z = x if x < y else y






#循环语句
#break, continue
#循环里的else
count = 0
while (count < 5):
	if count == 2:
		count += 1
		continue
	if count == 5:
		break
	print "haha%d"%count
	count+=1
else:
	print "I am else"    #如果循环里面没有执行break，则循环结束会执行else



#for循环遍历序列

aSeq = ['kobe','mj','shaq','curry']

for name in aSeq:
	print name,
print
for i in range(len(aSeq)):
	print aSeq[i],
print 
for i, name in enumerate(aSeq):
	print i,name,'\t',
print

print range(1,4,2)
print range(4)
print range(2,4)


#在需要语句的地方不写语句，解释器会提示语法错误，所以pass语句出现了

def foo():
	pass










#迭代器器器
#__iter__ next



#可迭代的：实现了 __iter__()方法
#迭代器：一个有__iter__()合next()方法的对象

#判断是否可迭代
e = enumerate(['a', 'b'])
from collections import Iterable  #collections库
print isinstance(e, Iterable)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

f = Fib()
print 'judge  ',isinstance(f, Iterable)


#序列迭代
#创建序列迭代器
aList = [123, 'xyz', 45.67]
fetch = iter(aList)
print type(fetch)

#遍历
while 1:
	try:
		i = fetch.next()
		print i,
	except StopIteration:
		print ''
		break

fetch = iter(aList)
for i in fetch:
	print i,
print ''



#创建字典的迭代器
aDict = {'a':1, 'b':2}
print aDict.iterkeys()
print aDict.itervalues()
print aDict.iteritems()


#文件的迭代器
#文件迭代器自动调用readline()方法
myFile = open("README.md")
for i in myFile:
	print i

#在迭代可变对象时，尽量不要修改可变对象
aTest = {'a':1, 'b':2, 'c':3, 'd':4}
try:
	for i in aTest:
		if i=='a' or i == 'c':
			aTest.pop(i)
except Exception,e:    #会抛出异常
	print e


#列表推导式
rect = [(x,y)for x in range(2) for y in range(3)]
print rect

#计算文件中单词个数
f = open("README.md")
print len([word for line in f for word in line.split()])
#查看文件大小
import os
print os.stat('README.md').st_size

#查看文件中字母的个数
f.seek(0)
print sum([len(word) for line in f for word in line.split()])


#生成器：一个内存使用更友好的结构
f.seek(0)
print sum((len(word) for line in f for word in line.split())) #使用生成器计算文件字符个数

rectProduct = ((x,y)for x in range(2) for y in range(3)) #将列表推导式改成生成器
for i,j in rectProduct:
	print i,j
		













