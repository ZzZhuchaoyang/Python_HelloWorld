"""布尔值"""
performance = 80
isA = performance >= 90
isB = performance >= 75 and performance < 90
isC = 60 <= performance < 75
isD = performance < 60

# The student's grade is 90,
print("The student's grade is", performance)
# isA is True,
print('isA is ', isA)
# isB is False ……

