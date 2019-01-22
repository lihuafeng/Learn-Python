# python
python学习笔记

序列解包
---

将多个变量同时赋值的方法称为序列解包(sequence unpacking)。因为采用这种方式赋值时，等号两边的对象都是元组。
```
x,y,z = 1,2,"hello world"
print x,y,z #1 2 hello world

y,x = x,y
print x,y  #2 1
```
 Python的多元赋值方式可以实现无需中间变量交换两个变量的值。

生成斐波那契數列
---
    斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。用计算机程序输出斐波那契數列的前 N 个数是一个非常简单的问题
https://github.com/lihuafeng/python/blob/master/demo1.py
