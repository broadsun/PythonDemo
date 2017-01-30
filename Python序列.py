# -*- coding:utf-8 -*-

__author__ = "Sun Guangbo"

'''
序列：字符串、列表、元祖
'''

p1 = ["kobe"]
p2 = ["curry"]
#连接操作符+, 
p3 = p1+p2
print p3
#extend更节省内存空间
p1.extend(p2)
print p1

#重复操作符
p1 = p1*2
print p1

#切片
print p1[-2::-2]

s= "abcde"
for i in range(len(s)):
    print s[:len(s)-i]

#工厂函数 list，str，tuple
#实际上没有进行类型转换，只是将对象作为参数，将内容拷贝到新生=生成的对象中
aList = [1,2,3]
print tuple(aList) #拷贝了一个指向[1,2,3,4,5]的索引，传递给tuple函数，生成了一个tuple对象


#enumerate(seq)返回一个元祖（index，value）
for i, j in enumerate(aList):
    print i,j

#max(seq)或者max(argv1,argv2...) 返回序列中的最大值
#min() 返回序列中的最小值
print max([1,2,3,4,999])
print max(1,2,3,4,999)

#reversed(seq)返回一个迭代器
for i in reversed([11,22,33]):
    print i

#sum(seq)返回和
print "sum is %d" % sum([1,2,3,4,5])

#zip(seq1,seq2)或者 zip(seq)
#返回一个由元祖构成的列表
print zip((1,2,3),(4,5,6))
print zip([1,2,3])













'''


字符串串串串串串串串串串串串串串
(普通字符串 和 Unicode字符串)


'''


#string模块
import string
print string.uppercase
print string.lowercase
print string.letters
print string.digits

#字符串的连接
#不推荐使用+
s1 = "sgb"
s2 = "SYC"
print "%s%s" % (s1, s2)
print "".join((s1, s2))
print s1.upper()
print s2.lower()

#格式化，即格式化成字符串
#格式化成16进制
print "%#x" % 128
#浮点数，精确到小数点后位数
print "%.3f" %1.234
#%在字符串中 %%这样表示
print "We are %d%%" % 100
#格式化可以用来修改字符串
s1 = "S%s" %s1[1:]
print s1

#字典参数格式化
print "I love buying %(label)s shoes" % {"label":"AJ"}


#新的字符串模板（我没用过），利用了string模块中的Template
from string import Template
s = Template("I love buying ${label1} shoes, and I don't like ${label2} shoes")
print s.substitute(label1 = 'AJ', label2 = 'adidas') #substitute,两个键值必须都指定
print s.safe_substitute(label1 = 'AJ') #safe_ubstitute,两个键值不需要都指定

#原始字符串，按照字面意思使用字符串，不存在转译字符或不能打印的字符
print r"\t\n\\"

print isinstance('xxx', str)
print isinstance(u'xxx', unicode)
print isinstance('xxx', basestring)


#python字符可以直接比较
teststr = 'f'
if 'z'>= teststr >= 'a':
    print "sss"

#字符串的比较cmp(str1,str2)
print cmp('sgb','syc')
print cmp('sgb','SYC')


#字符串的内建方法
teststr = "  baby,how are you, baby? \n"
#去除两边空格合换行符，如果去除右边rstrip()，左边lstrip()
teststr = teststr.strip()

print teststr.capitalize() #首字母大写
print teststr.title()      #每个单词首字母大写
print teststr.count('o') #字符串中某个字符的个数

#查找从0到结尾中，baby子串出现的首个位置,可以指定起始位置
#没找到返回-1
print teststr.find('babys',0,5)
#查找'you'在字符串中出现的首次位置，与find类似
#没找到抛出异常，推荐使用find
print teststr.index('you',0,len(teststr))

print teststr.decode(encoding='UTF-8') #以encoding指定格式解码字符串
print teststr.encode(encoding='UTF-8') #以encoding指定格式编码字符串
print teststr.endswith('baby') #是否以baby结束
print teststr.replace('baby', 'syc') #将baby替换成syc
print teststr.replace('baby', 'syc', 1) #将baby替换成syc，替换 1 次

#分割和连接
#以某个字符分割字符串,可以指定分割几次
print teststr.split(' ')
print teststr.split(' ', 1)
#首字母大写，自己写，哈哈
daxie = "sgb"
daxie1 = ''.join((chr(ord(daxie[0])-32),daxie[1:]))
print daxie1


#------------------------------------
#Unicode VS ASCII
#------------------------------------

#Unicode字符串  types.UnicodeType
print unicode(97) #相当于ASCII的str()
#输入数字，输出对应unicode字符
print unichr(97)  #相当于ASCII的chr()
#Unicode多有种编码方式


#ASCII字符串 types.StringType
#输入0~255，输出对应字符
print chr(97)
#输入字符，输出ASCII
#支持unicode
print ord('s')
print ord(u'孙')



'''


#列表 表表表表表表表表表表表表表表表表表表表表表
#list


'''

aList = [7,4,6,0,9]

#删除列表元素，3种
del aList[3]
print aList
aList.remove(6) #remove(val) ：参数是值
print aList
aList.pop() #pop(index) :参数是索引，默认是最后一位
print aList

#列表的内建函数
#append(object)可以传入任一个对象
#extend(seq) 只能传入可迭代对象
aList = [1,'sgb',2, 'syc']
aList.insert(2, 'baby')  #在指定位置插入
print aList
aList.append(['append', 3]) #在末尾追加元素, append(object)
print aList
aList.extend(['extend',3]) #延长列表 , append(iterable object)
print aList
aList.extend('sgb') #延长列表 , append(iterable object)
aList.extend(reversed('sgb')) #延长列表 , append(iterable object)
print aList

#排序和翻转
aList.sort()
print aList
aList.reverse()
print aList

##!!可以改变对象值的可变对象的方法是没有返回值的
## pop除外，pop既可以改变列表的值，也返回pop出的值
'''

sort(), reverse(), extend(), append(),insert()

'''

# 列表可以模拟 堆栈 和 队列

#入栈
aList.append("push")
#出栈
aList.pop()
print aList

#入队
aList.append("pushback")
#出队
aList.pop(0)

print aList





'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


#元组组组组组组组组组组组组组组组组
#tuple

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#所有多对象的、逗号分隔的、没有明确用符号定义的，这些集合默认类型都是元祖
#单个元素的元祖
singleTuple = ('xyz',)
print type(singleTuple)





#浅拷贝 vs 深拷贝
person = ['name', ['saving', 100]]
hubby = person[:]
wifey = list(person)

hubby[0] = 'sgb'
wifey[0] = 'syc'
print hubby,wifey

hubby[1][0] = 'money'
wifey[1][1] = 500
print hubby, wifey


sgb = ['sgb', 25, ['c++', 'python', 'php']]
syc = sgb
print id(sgb), id(syc)  #两个对象一样， sgb is syc, sgb[i] is syc[i]

#浅拷贝
#切片[:]
#工厂函数
#copy.copy
import copy
syc = copy.copy(sgb)
print id(sgb), id(syc)          #sgb is not syc
print [id(x) for x in sgb]      #sgb[i] is syc[i]
print [id(y) for y in syc]

syc[0] = 'syc'
syc[2].append('java')
print sgb,'\n',syc   #对于不可变对象，改变时会使用一个新的对象

#深拷贝
sgb = ['sgb', 25, ['c++', 'python', 'php']]
syc = copy.deepcopy(sgb)
print id(sgb),id(syc)			#sgb is not syc
print [id(x) for x in sgb]		#sgb[2] is not syc[2]
print [id(x) for x in syc]		#对于原子类型，没有拷贝这一说，注意观察id(sgb[0]) 和 id(syc[0])

#如果元祖类型对象只包含原子类型对象，则不深拷贝
test=(1,2,3)
testcopy = copy.deepcopy(test)
print testcopy is test   #深拷贝函数后，两者id还是要一样，说明没有深拷贝


#这里的疑问就是对象不一样，对象的内容一样，这两个不是捆绑在同一块内存空间嘛？？？？？？？？？？？？？？？？？？？？

























