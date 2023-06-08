#generator

def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a+ b

result = fibonacci(100)
print(result)
print(next(result))

for num in result:
    print(num)