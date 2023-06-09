class Mobile:
    fp ='yes' #class member 변수

realme = Mobile()
redme = Mobile()
geek = Mobile()

#class name space
print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)

Mobile.fp = 'no'
print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)

realme.fp ='Not Working'
print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)