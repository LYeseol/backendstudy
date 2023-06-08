#dictionary
stu ={101:'Kim', 102:'Bae', 103:'Hong'}
fees={'kim': 2000, 'bae': 3000, 'hong': 8000}
print(stu[101])
print(stu[102])
print(stu[103])

print(fees['kim'])
print(fees['bae'])
print(fees['hong'])

stu[102]='python'
print(stu)
stu[104] ='멋쟁이사자'
print(stu)

del stu[102]
print(stu)
print(101 in stu)

new_stu = stu.copy()

key = (101,102,103)
value = '멋쟁이사자'
new_stu = dict.fromkeys(key, value)
print(new_stu)
print(stu.get(101))
print(stu[101])

print(stu.items())
print(stu.keys())
stu.update({104:'멋쟁이사자2'})
print(stu)
stu.pop(104)
print(stu)
print(stu.pop(104, 'No value'))
stu.setdefault(104, 'Park')
print(stu)


#
# #set
# a ={10,20,30}
# a ={10,20,30,'멋쟁이사자', 'Bae', 40}
# a = {10,20,30,'멋쟁이사자', 'Bae', 40, 10, 20}
#
# new_set = a.copy()
# b = set()
# print(type(b))
# a.add(50)
# a.update([10,20,60,70])
# print(a)
# a.remove('멋쟁이사자')
# a.discard('멋쟁이사자')
# a.discard(70)
# print(a)
#
#
# # new_set.clear()
# # print(new_set)
#
# intersection_a_new= a.intersection(new_set, a,b)
# print(intersection_a_new)
#
# union_a=a.union(new_set)
# print('union_a: ', union_a)
#
# diff_a=a.difference(new_set)
# print('diff_a: ', diff_a)
#
# print(a.issubset(new_set))
# print(a.issuperset(b))
# sym_a= a.symmetric_difference(new_set)
# print('symmetric_difference: ', sym_a)