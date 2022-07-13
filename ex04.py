#정수형

a=101
print(a,type(a))

#앞에 0b가 붙는 경우 이진수로 인식
b=0b101
print(b,type(b))

#8진수
c=0o101
print(c)

#16진수
d=0x101
print(d)


#10진수 --> 2진수, 8진수, 16진수
print(bin(5))
print(oct(65))
print(hex(257))

#파이썬 3.x 에서는 long형이 없어지고 int 타입으로 처리
e = 2**1024 #2의 1024승
print(e)
print(type(e))
