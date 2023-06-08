#
# def add(x, **num):
#     z= x+ num['a']+ num['b']+ num['c']
#     print('Addition: ', z)
#
# add(3, a=5,b=2,c=4,d=5)

def show():
    x = 10
    print(x)

show()

def add(y):
    x = 10
    print(x)
    print(x+y)

add(20)

a= 50
def show():
    x = 10
    print(x) #local
    print(a) #global

show()

print('Global variable a: ', a)
i = 0

def myfunc():
    a = i+1
    print("My function a: ", a)

myfunc()

print('Global variable a: ', a)

# # Example 1 - position arguement
# def add(x, y):
#     z = x + y
#     print('Addition: ', z)
#
#
# add(5, 2)
#
#
# # Example2
# def add(*num):
#     z = num[0] + num[1] + num[2]
#     print("Addition *: ", z)
#
#
# add(5, 2, 4)
#
#
# # Example 3
# def add(x, *num):
#     z = x + num[0] + num[1]
#     print('Addition (x+num*): ', z)
#
#
# add(5, 2, 4)
