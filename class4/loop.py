"""
for循环：知道执行次数或者知道执行的对象去指定的循环
"""

for i in range(5):
    print("current i is ", i)

print("123", end="")
for i in range(50, 60, 2):
    print("current i is ", i)
"""
while循环：知道执行条件的循环
"""

a = 1

while(a<5):
    print(a)
    a += 1  # a = a+1



from class4.ifEle import getScoreFunction
import random
todoScores = [91,90,58,98,30]
for todoScore in todoScores:
    result = getScoreFunction(todoScore)
    print(result)

for i in range(2):
    for j in range(3):
        print(i,j)

def testWhile():
    a = random.randint(0, 100)
    print(a)
    while a>=60:
        print(getScoreFunction(a))
        a = random.randint(0, 100)