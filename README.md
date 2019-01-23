# python
python学习笔记

运算符 //
---
地板除： // 除法不管操作数何种数值类型，总是舍去小数部分，返回数字序列中比真正的商小的最接近的数字。
```python
>>> 1//2
0
>>> 1.0//2.0
0.0
>>> -1//-1
1
>>> -1//1
-1
```
divmod()函数
---
 divmod函数把除法和区域运算结合起来，返回一个包含商和余数的元组。对整数来说， 它的返回值就是地板除和取余操作的结果。对浮点数来说，返回的商部分是math.floor(num1/num2)。
 ```python
 >>> divmod(10,3)
(3, 1)
>>> divmod(3,10)
(0, 3)
>>> divmod(10,2.5)
(4.0, 0.0)
>>> divmod(2.5,10)
(0.0, 2.5)
 ```

int(), round(), math.floor()不同之处：
---

函数 int()直接截去小数部分。（返回值为整数）

函数 floor()得到最接近原数但小于原数的整数。（返回值为浮点数）

函数 round()得到最接近原数的整数。（返回值为浮点数）

oct()和 hex()
---
提供了两个内建函数来返回字符串表示的8进制和16进制整数。它们分别是oct()和 hex()。它们都接受一个整数（任意进制的）对象，并返回一个对应值的字符串对象。
```python
>>> oct(1)
'01'
>>> hex(1)
'0x1'
>>> hex(8)
'0x8'
>>> oct(8)
'010'
```
序列解包
---
将多个变量同时赋值的方法称为序列解包(sequence unpacking)。因为采用这种方式赋值时，等号两边的对象都是元组。
```python
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

循环与else
---
Python中，可以在 while 和 for 循环中使用 else 语句。在循环中使用时， else子句只在循环完成后执行， 也就是说 break 语句也会跳过 else 块。
以寻找最大约数为例, 代码如下：
```python
def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d is %d' % (num,count)
            break
        count -= 1
    else:
        print num,"is prime"
```
同样地，for 循环也可以有 else 用于循环后处理。 它和while 循环中的else 处理方式相同。 只要for 循环是正常结束的(不是通过 break )， else 子句就会执行。

创建迭代器
---
格式：
* iter(obj)
* iter(func,  sentinel)
1 如果传递一个参数给 iter() ,它会检查你传递的是不是一个序列,如果是,那么很简单：根据索引从 0 一直迭代到序列结束。另一个创建迭代器的方法是使用类：一个实现了__iter__() 和 next() 方法的类可以作为迭代器使用。 
2 如果是传递两个参数给iter() ,它会重复地调用 func ,直到迭代器的下个值等于sentinel。
```python
def fun():
    return 2
if __name__ == "__main__":
    item= iter(fun,2)
    for i in item:
        print i
 #当fun return 2，没有输出。当fun return 1,输出1，死循环
```
