#List 실습

fruits = ['apple', 'banana', 'cherry', 'orange']
vegi = ['carrot', 'cucumber']

grocery = fruits + vegi
print(grocery)

#sorting function
numbers = [10,5,8,1,7]
numbers.sort()
print(numbers)

#slicing
slice_num = numbers[1:4]
print(slice_num)

#copy list
numbers_copy = numbers.copy()
print('numbers_copy',numbers_copy)
numbers_copy.pop()
print('numbers',numbers)
numbers_copy = numbers[:]
print(numbers_copy)