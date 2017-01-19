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

#输入0~255，输出对应字符
print chr(97)
#输入字符，输出ASCII
print ord('a')

#python字符可以直接比较
teststr = 'f'
if 'z'>= teststr >= 'a':
    print "sss"

#字符串的比较cmp(str1,str2)
print cmp('sgb','syc')
print cmp('sgb','SYC')


#字符串的内建方法
teststr = "  baby,how are you, baby?  "
#去除两边空格，如果去除右边rstrip()，左边lstrip()
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




























