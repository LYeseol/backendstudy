import array
stu_roll= array.array('i', [101,102,103,104])

for i in stu_roll:
    print(i)

n = len(stu_roll)
for i in range(n):
    print(i , ' = ' ,stu_roll[i])