from array import *

print('parameter가 없는 함수')
def disp():
    name ='lion'
    print('welcome to ', name)


def add(y):
    x=10
    c=x+y
    print(c)
    print(f'formatted output {x+y: }')

add(20)


#
# stu_roll = array('i', [101,102,103,104,105,106,107])
# print('배열 슬라이싱')
# n= len(stu_roll)
# for i in range(n):
#     print(i,'= ', stu_roll[i])
#
# a = stu_roll[1:5]
# for i in a:
#     print(i)
#
# print('5까지')
# a = stu_roll[:5]
# for i in a:
#     print(i)
#
# print('마지막 4개')
# a = stu_roll[-4:]
# for i in a:
#     print(i)
# print('마지막 1개 빼고')
# a = stu_roll[:3]
# for i in a:
#     print(i)

# print('remove after pop()')
# stu_roll.pop()
# n = len(stu_roll)
# i=0
# while i< n:
#     print(stu_roll[i])
#     i+=1

# while i<n:
#     print(stu_roll[i])
#     i+=1
#
# print("array after insert")
# stu_roll.insert(1, 106)
# stu_roll.insert(3, 107)
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1
#
# print('remove after')
# stu_roll.remove(101)
# i=0
# while i< len(stu_roll):
#     print(stu_roll[i])
#     i+=1
