def val(lst):
    print("Inside function before append: ", lst, id(lst))
    lst.append(4)
    print("Inside function after append", lst, id(lst))
lst = [1,2,3]
print('Before calling function: ', lst, id(lst))
val(lst)
print('after calling function: ', lst, id(lst))

