# 문자열 관련 함수

# replace : 문자열 교체 함수
# 입력값 : 원본문자, 새로운문자
print("banana".replace("a","o")) #bonono

# 전화번호에서 -하이픈을 :로 교체
# 입력값 : 교체대상, 새로운문자
print("010-1234-5678".replace("-",":")) #010:1234:5678

# 전화번호에서 - 하이픈을 제거
print("010-1234-5678".replace("-","")) #010:1234:5678

# repr : 따옴표를 표시하는 함수
print("hello") #hello
print(repr("hello")) #'hello'

# 공백 제거 함수들
print(repr(" hello world ".strip())) #'hello world'
print(repr(" hello world ".lstrip())) #'hello world '
print(repr(" hello world ".rstrip())) #' hello world'

# title : 첫글자만 대문자로 바꾸는 함수
print("hello world".title()) #Hello World