# int float bool str
a = "1"
b = "2"
# 형 변환 (type casting) 
c = int(a) 
d = int(b)
print(a+b)
print(type(a+b))
print(c+d)
print(type(c+d))

# 실수를 정수로 변환
a = 1.5
b = int(a) # 소수점 아래를 버리고 정수만 남깁니다.
print(type(a))
print(type(b))

# 문자열 데이터를 정수로 변환
c = "100"
d = int(c)
print(type(c))
print(type(d))

a = True
b = False
f = int(a)
e = int(b)
print(f)
print(e)

# 실수형 데이터로 변환
a = 10
b = float(a)
print(b)

# 문자열 형 변환
a = 12
b = "3"
print(str(a) + b)
# bool 형 변환
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("123"))