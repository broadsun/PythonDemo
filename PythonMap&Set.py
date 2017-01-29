# -*- coding:utf-8 -*-

__author__ = "Sun Guangbo"





'''



字典典典典典典典典典典典典典典典典典典典典典典典典典典典典典典典典典典典典典
dict



'''


#字典是Python中唯一的映射类型

dict1 = {'sgb':1, 'syc':2}
dict1 = dict([('sgb',1),['syc',2]]) #dict工厂方法里面是一个序列的序列
dict1 = dict(zip(('sgb','syc'),(1,2)))
dict1 = dict(sgb=1, syc=2)  #key word can't be expression, sgb没有引号呦
print dict1

dict2 = dict(**dict1)  #可以接受关键字参数，平时不怎么用
print dict2

dict3 = dict1.copy()  #这个比传入关键字参数效率要高
print dict3

#创建一个value相同的字典
dict1 = {}.fromkeys(('sgb','syc')) #默认值None
print dict1
dict1 = {}.fromkeys(('sgb','syc'),-1)
print dict1



#遍历一个字典，可以循环查看键
for key in dict1:
	print key, dict1[key]

#增加新元素
dict1['kobe'] = 24

#删除字典元素
del dict1['sgb']
dict1.pop('syc')
dict1.clear()  #清空键值对，但字典还在
print dict1
del dict1  #删除字典


aDict = {'sgb':25, 'syc':30,'curry':30, 'kobe':24}
#是否存在key-value对
print 'sgb' in aDict
print 'lbj' not in aDict


#字典的比较（没用过）
dict1 = {'sgb':1,'syc':2}
dict2 = {'curry':30, 'kobe':24, 'mj':23}
print cmp(dict1,dict2)

#比较算法按照下面的顺序
'''
1、字典key的个数越多，字典越大
2、比较字典的key，比较顺序和keys()返回的顺序一致
3、比较字典的value
'''

#返回可哈希对象的哈希值
print hash("sgb")

#返回映射对象的长度
print len(dict2)

print dict2.keys()
print dict2.values()
print dict2.items()


#update(newDict)
aDict.update({'kobe':8, 'mrh':25}) #将参数里的字典更新到dict2
print aDict

#get(key, default = None)
print aDict.get('kobe')
print aDict.get('xxx')     #不存在默认返回None，不会抛出异常
print aDict.get('xxx', 'haha')

#setdefault(key, default = None) 
#如果key存在返回对应的value，否则设置dict[key]=value,并返回value
#第二个参数可有可无
print aDict.setdefault('lbj',6)
print aDict
print aDict.setdefault('sgb')

#key必须是可哈希的
#不可变对象一定是可哈希的，数字，字符串，元祖（只含有数字和字符串的元祖）
#可变对象，如果实现了__hash__()特殊方法，返回一个不可变对象，那么也是可哈希的




'''



集合合合合合合合合合合合合合合合合合合合合合合合合
set



'''

#集合对象是一组   无序排列的 值
#可变集合不是可哈希的
#不可变集合是可哈希的


#创建set
aSet = set("sgbsyc")
aFSet = frozenset('sgbsyc')
print aSet
print aFSet

for i in aSet:
	print i,
print


#更新可变Set
aSet.add('mrh')   #增加一个新成员，add（一个元素）
print aSet

aSet.update('curry')  #用一个集合来update，update（一个集合）
print aSet

#删除可变集合集合元素

aSet.remove('s')  #remove(一个元素)
aSet -= set('sgb')   #减去一个集合
print aSet


#子集，严格子集
print set('sgb') < set('sgbc')
print set('sgb') <= set('sgbbbbb')



#联合，交集，补集，异或
s1 = set('sgb')
s2 = set('syc')

print s1|s2
print s1&s2
print s1-s2
print s1^s2


























































