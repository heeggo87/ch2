# 문자열 만들기
print("hello")

# 문자열 자르기
# 문자열 안에서 문자하나를 추출
# 문자열 [index]
# index란? 문자의 위치
# 무조건 0부터 시작이며 연속적
print("hello"[0]) #h
print("hello"[1]) #e
print("hello"[2]) #l
print("hello"[3]) #l
print("hello"[4]) #o

# 문자 슬라이드
# [index] => 문자하나만 추출
# [index시작:index끝] => 범위로 추출
# 슬라이스에서 끝번호는 포함x
print("hello"[0:2]) #he

# 2부터 마지막
print("hello"[2:5]) #llo
print("hello"[2:]) #llo

# 처음부터 2까지
print("hello"[:2]) #he

# 전체
print("hello"[:]) #hello

# 문자열의 길이를 구하는 함수 : len
print(len("aaa")) #3
print(len("hello, world!")) #13, 공백도 문자로 취급
print(len("안녕하세요")) #5
