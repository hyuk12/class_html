# 사용자 지정함수(메소드)
# 사용자가 직접 만든 함수

# 함수 용어 정리
#  함수를 정의 한다 : 사용자 함수를 새로 만든다
#  인수 : 사용자 함수에 전달할 입력값 (argument)
#  매개변수 : 인수를 받아서 저장하는 변수(parameter)
#  반환값 : 사용자 함수의 출력 의미 (return)
#  함수호출 : 만들어진 함수를 실제로 사용하는것

# #  함수의 정의
# def 함수이름(매개변수):
#     기능, 본문
#     return 반환값

# def func (n,m) :
#     result = n + m
#     return print(result)

# func(0,1)

# 지역변수 , 전역변수
#  지역변수 : 함수내에서 쓰는 변수(local variable)
#  전역변수 : 프로그램 전체에서 쓰는 변수(global variable)

def func():
    vars = "Hello Python"
    print(vars)
vars = "Hello Java"
func()
print(vars)
