# 형변환이 필요한 이유

# 더하기를 하기 위해서 str 을 int 로 변환
# 두항의 타입이 일치하지 않으면 에러남
print(int("10") + 20) # int + int = 30

print(float("3.14") + 1.1) #float + float = 4.24

# 100원을 만들고 싶음
print(str(100) + "원") #str + str = 100원
