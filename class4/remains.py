"""
类 class：作为特殊的对象实现共有功能与差异化的功能
"""
class A:
    def __init__(self):
        pass

    def __int__(self):
        return 2

class B(A):
    def __init__(self):
        super(self)

a = A()
print()
print(a)  # <__main__.A object at 0x0000028EC578AF10>

"""
函数 definition
"""

def add(a,b):
    return a+b

add(5,6)
c = add(5, 6)
print(add(5,6))

"""
import
"""

import sys
sys.stdout.write("always")

from class3.stringFunction import performance
print(performance)
from sys import stdout

"""
python三个特有的数据结构
1.列表list：[]
2.集合set：()
3.字典dict:{}
"""
list1 = [1,2,3]
list2 = list()
list1.append(6)
list1.remove(2)
# ...
set1 = set()
set2 = (1,2)
# ...
dict1 = { "a" : 1 }
dict1["a"]
print(dict1)
print(dict1["a"])




