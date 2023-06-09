class Vector(object):
    def __init__(self,x,y):
        #instance variable
        self.x = x
        self.y = y

    #연산자 오버로딩- 클래스 내에서 같은 이름의 메소드를 여러 개 선언, 상속 관련 x
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    #연산자 오버라이딩==> 기존 메소드 변경
    def __str__(self):
        return f'Vector({self.x}, {self.y})'

a = Vector(1,2)
b = Vector(3,4)

print(a)
print(b)
print(a+b)
