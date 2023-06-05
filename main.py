a=5
b=2
c=3
d=200

print('AND 연산자')
print('a:%d  b: %d' %(a,b) )
print('a>b and a<c: ', a>b and a>c)
print('a>b and a<c: ', a>b and a<c)

print('OR연산자')
print('a>b and a<c: ', a>b or a>c)
print('a>b and a<c: ', a>b or a<c)

print('NOT 연산자')
print('a:%d  b: %d c:%d' %(a,b,c) )
print('not(a<b): ', not(a<b) )
print('not(a<c): ', not(a<c))
