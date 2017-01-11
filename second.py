# -*- coding:utf-8 -*-
__author__ = "Sun Guangbo"

import decimal

'''
1、输入输出
2、注释
3、操作符
4、变量与赋值
5、数据类型
6、缩进
7、循环与条件
8、文件
9、错误
10、函数
11、类
12、模块
'''
if __name__ == '__main__':
	#字符串格式化
    print "%s is number %d" % ("Python", 1)
    '''
    Python数字类型
    int：不会溢出，会自动转换成长整形
    long:仅受限于计算机虚拟内存
    bool
    float
    complex
    decimal：用于十进制浮点型
    '''
    print decimal.Decimal('1.1')
    print 3**3 #幂次方

    print "//////////字符串//////////"
    
    pystr = "Python"
    print pystr[0]
    print pystr[2:7]
    print pystr+" is king" #字符串拼接
    print pystr*2 #字符串重复
    print '-'*20

    print "//////列表元祖字典//////"
    aList = [1,2,3,"ss"]
    aList[-1] = 'ssss'
    print aList[2:]
    aTuple = ("sss",2,3,"haha")
    aDict = {'sgb':1}
    aDict['syc'] = 2
    print aDict
    print aDict.keys()
    print aDict.values()

    print "///////语句//////"
    testStr = "syc"
    if testStr == 'syc':
        print "str is syc"
    elif testStr == 'sgb':
        print "str is sgb"
    else:
        print "NULL"

    counter = 0;
    while counter != 3:
        print "counter is %d"%counter
        counter+=1

    for i in aList:
        print i
    for i in range(len(aList)):
        print aList[i]

    print "//////打开文件与错误异常//////"

    try:
        filename = raw_input("Enter file name: ")
        fd = open(filename,'r')
        for line in fd:
            print line
        fd.close()
    except IOError, e:
        print 'file open error',e

    print "//////函数和类//////"
    
    def foo(debug=True)：
        if debug:
            print "In Debug"
        else
            print 'In Release   '
    class FooClass(object):
        #静态变量version
        version = "0.1"
        def __init__(self):
            self.__name = "sgb"
        def showname(self):
            print self.__name
    







