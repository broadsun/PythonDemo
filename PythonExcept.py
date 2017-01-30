#-*- coding:utf-8 -*-

__author__ = 'Sun Guangbo'




#处理多个异常
def safe_float(obj):
	try:
		res = float(obj)
	except ValueError, e:
		res = "ValueError"
	except TypeError, e:
		res = "TypeError"
	finally:
		return res

print safe_float({})
#print safe_float("syc")


#同时处理多个异常
def safe_float(obj):
	try:
		res = float(obj)
	except (ValueError,TypeError), e:
		res = e
	finally:
		return res

#print safe_float({})




#BaseException  #所有异常的基类
#Exception 常规错误
# from time import sleep
# try:
# 	while(1):
# 		print "haha"
# 		sleep(2)
# except BaseException,e:  #BaseException可以捕获所有异常，包括 KeyboardInterupt, SystemExit
# 	print e


#上下文管理
with open('README.md') as fr:  #不需要显式调用close()
	for line in fr:
		print line.strip()

#如何定义一个类，使其可以和with协调工作
#模块contexlib可以帮助编写上下文管理器
#__context__(), __enter__(), __exit__()



#主动触发异常,后面必须是 old-style classes or derived from BaseException
raise NameError
class classNew(Exception):
	pass
raise classNew()


#断言，后面的表示为True，不采取措施，否则出发AssertionError
assert 1==1   #True,nothing happen
assert 'sgb' is 'syc'  #False, raise AssertionError

#assert的简单实现
def assert(expr, args=None):
	if __debug__ and not expr:
		raise AssertionError, args

#sys模块来显示异常信息
try:
	float("123sgb")
except:
	import sys
	exc_tuple = sys.exc_info()
	print exc_tuple #(异常类，异常类实例，跟踪记录对象)

