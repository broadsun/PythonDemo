# -*- coding:utf-8 -*-
class testDir(object):
#__slots__ = ['classAttr','instanceAttr']
	def __init__(self):
		self.instanceAttr = 1
	classAttr = 2

testDir.classAttr1 = 3
if __name__ == '__main__':
	x = testDir()
	print "dir(x) is :  ", dir(x)
	print 'class __dict__ is ', testDir.__dict__
	print 'instance __dict__ is :  ',x.__dict__