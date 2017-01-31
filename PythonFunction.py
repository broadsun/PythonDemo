# -*- coding:utf-8 -*-

__author__ = 'Sun Guangbo'

'''
函数返回值个数对应的类型：
0：		None
1：		对象
大于1：  元祖

'''

def foo():
	'function test doc'
	pass
print foo.__doc__
foo.version = 0.1
print foo.version
print dir(foo)

#通过上面的例子，又一次证明了，一切皆为对象，函数也是对象





##########################################
print "内嵌函数&&装饰器"
##########################################

#内嵌函数

def foo():
	def bar():
		print "bar called"
	print "foo called"
	bar()

#装饰器
'''
@deco
def func(argv1):
	pass
func = deco(func)

@deco2
@deco1
def func(argv1):
	pass
func = deco2(deco1(func))

@deco(deco_args)
def foo(argv1):
	pass
foo = deco(deco_args)(foo)


@deco1(deco_args1)
@deco2(deco_args2)
def foo(argv1):
	pass
foo = deco1(deco_args1)(deco2(deco_args2)(foo))

'''

'''
函数的关键字参数和位置参数可以混用，位置参数放在关键字参数前面
参数定义的顺序必须是：必选参数、默认参数、可变位置参数和可变关键字参数
def test(name, age, sex='male',*args,**kwargs):
定义函数，参数前有*，收集位置参数形成元祖，** 收集关键字参数形成字典
使用函数，参数前有*，分解元祖成位置参数，参数前有**，分解字典成关键字参数，解包

'''

# output = '<int %r id=%#0x val=%d>'
# w=x=y=z=1
# def f1():
# 	x=y=z=2
# def f2():
# 	y=z=3
# 	def f3():
# 		z = 4
# 		print output % ('w',id(w),w)
# 		print output % ('x',id(x),x)
# 		print output % ('y',id(y),y)
# 		print output % ('z',id(z),z)
# 	clo = f3.func_closure
# 	if clo:
# 		print "f3 closure vars: ",[str(c) for c in clo]
# 	else:
# 		print "no f3 closure vars"
# 	f3()
# 	clo = f2.func_closure
# 	if clo:
# 		print "f2 closure vars: ",[str(c) for c in clo]
# 	else:
# 		print "no f2 closure vars"
# f2()
# clo = f1.func_closure
# if clo:
# 	print "f1 closure vars: ",[str(c) for c in clo]
# else:
# 	print "no f1 closure vars"
# f1()


#装饰器的使用，我反正写不出来
from time import time
def logged(when):
	def log(f, *args, **kwargs):
		print '''Called:
		function: %s
		args: %r
		kwargs: %r''' % (f,args,kwargs)
	def pre_logged(f):
		def wrapper(*args, **kwargs):
			log(f,*args, **kwargs)
			return f(*args, **kwargs)
		return wrapper

	def post_logged(f):
		def wrapper(*args, **kwargs):
			now = time()
			try:
				return f(*args, **kwargs)
			finally:
				log(f,*args, **kwargs)
				print "time delta: %s" % (time()-now)
		return wrapper

	try:
		return {'pre':pre_logged,'post':post_logged}[when]
	except KeyError, e:
		raise ValueError(e),'must be pre or post'

@logged("post")
def hello(name):
	print "Hello ", name
hello("world")


#生成器的优势，可以保留上下文环境，比如你在处理A事务时，转去处理B，处理完B之后，回到A需要继续执行，这时next函数就派上用场了

#生成器的send合yield

def counter(start_at = 0):
	count = start_at
	while 1:
		val = (yield count)
		if val:
			count = val
		else:
			count+=1
try:
	g = counter(3)
	print g.next()  #yield count的返回值为None
	print g.next()
	print g.send(10)  #调用send后，yield count的返回值为send的参数值，这里是9
	print g.next()
	g.close()
	print g.next()
except BaseException,e:  #BaseException可以捕获所有异常，包括 KeyboardInterupt, SystemExit
 	print "Exception happen"

















