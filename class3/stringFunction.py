"""布尔值"""
performance = 95  # 分数
isA = performance >= 90
isB = performance >= 75 and performance < 90
isC = 60 <= performance < 75
isD = performance < 60

# The student's grade is 90,
print("The student's grade is", performance, 'isA is', isA)


# 通配符顺序填充
"""
顺序填充字符串里存在几个{}，并且按照format里参数的顺序进行填充
并且字符串里有几个{}，format就传几个参数
"""
print("The student's grade is {} isA is {}".format(performance, isA))

#通配符序号填充
"""
通配符里带数字，并且format中参数数量等于通配符中最大的数字

序号从0开始， 自然数  -->  {n} n>=0, Z
按format中参数的顺序，从序号0开始，由小到大填充
"""
print("{0}\t{1}\t{0}".format("通配符第一个", "通配符第二个"))  # 通配符第一个	通配符第二个	通配符第一个

print("{}\t{}\t{}".format(0 ,1 ,0))  # 通配符顺序填充
print("{0}\t{1}\t{0}".format('b', 'A'))

print("The student's grade is {0} isA is {1}".format(performance, isA))
print("The student's grade is {1} isA is {0}".format(isA, performance))


str_a = "  abcdefg; hijklmn    \n"
print(str_a)

print(str_a.replace(';', '\n'))
print(str_a.replace('abefg', 'ABCDEFG'))  #replace是在原字符串里寻找旧字符串，如果找到第一个旧字符串，则换成新字符串，如果没找到就不换
print(str_a.replace('abcdefg', 'ABCDEFG'))

print(str_a.strip(), end="|\n")
print(str_a.lstrip(), end="|\n")
print(str_a.rstrip(), end="|\n")

print('a' in str_a)
print('ab' in str_a)


# 小练习： 将str_a中空格替换为非空格
print(str_a.strip(' '))
print(str_a.replace(' ', ''))
