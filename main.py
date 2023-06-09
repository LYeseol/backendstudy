class ParentClass:
    def __init__(self):
        self.name = 'parent'
        self.number = 10

    def __str__(self):
        return f'ParentClass name: {self.name}, numer:{self.number}'
    def add_num(self,new_number):
        print('부모: ', new_number, '만큼 더 해야지')
        self.number = self.number + new_number
class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.name='child'
    def __str__(self):
        return f'Childclass name: {self.name}, number: {self.number}'
    def add_num(self,new_number):
        print('고정적으로 5 더할건데?')
        self.number = self.number +5


parent = ParentClass()
child = ChildClass()
# print(parent)
# print(child)

print('7을 더하세요')
parent.add_num(7)
child.add_num(7)
print(parent)
print(child)