# -*- coding: utf-8 -*-
# 输出斐波那契數列

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        print b
        a,b = b,a + b
        n = n + 1
fab(5)
print "------"
def fab1(max):
    n,a,b = 0,0,1
    L = []
    while n < max:
        L.append(b)
        a,b = b,a + b
        n = n + 1
    return L
for i in  fab1(5):
    print i
print "------"
# iterable 对象
class Fab(object):
    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b = 0,0,1
    def __iter__(self):
        return self
    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration() #结束iterator.next()
for i in Fab(5):
    print i
print "------"
# yield
def fab2(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n=n+1

for i in fab2(5):
    print i

from inspect import isgeneratorfunction
print isgeneratorfunction(fab2) #True  判断一个函数是否是一个特殊的 generator 函数

# fab2 是一个 generator function，而 fab2(5) 是调用 fab2 返回的一个 generator，好比类的定义和类的实例的区别
import types
print isinstance(fab2,types.GeneratorType)
print isinstance(fab2(5),types.GeneratorType)
