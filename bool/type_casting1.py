# 형변환
# 자료형을 다른 자료형으로 바꾸는 것

print(3.23, type(3.23)) #3.23 float(실수)

# float -> int
print(int(3.23)) #3

# 문자열 "323"
print("323", type("323")) #str

# str -> int
print(int("323")) #323 -> 323

# int -> float
print(float(323)) #323 -> 323.0

# 문자열 "3.23"
# str -> float
print(float("3.23")) #"3.23" -> 3.23

# int -> bool
print(bool(0)) #False 0만 거짓
print(bool(1)) #True
print(bool(2)) #True

# int -> str
print(str(123)) #123 -> "123"

# float -> str
print(str(3.14)) #3.14 -> "3.14"

# 형변환이 필요한 이유?
# int float bool str
# 어떤값을 계산하기 위해서 