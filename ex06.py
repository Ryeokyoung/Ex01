#복소수

#복소수 타입의 객체는 실수부+허수부로 나뉘며 허수부에는 j또는 J

a=4+5j
print(a,type(a))

a=4+5j
b=7-2j
print(a+b)

print(b.real)#7.0
print(b.imag)#-2.0

c=4
d=5.4

print(type(complex(c)))
print(type(complex(d)))

print(c)    #-형이 아예 바뀐건 아님