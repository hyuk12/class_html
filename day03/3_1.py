#  if while for
# if 문
#  만약에 ...

#  조건이 만족되면 실행

#  사용자로부터 하나의 숫자를
#  입력받고 짝수/ 홀수를 판별하라

# num = int(input("숫자를 입력해주세요 : "))

# if num % 2 == 1 :
#     print("홀수 입니다")
# else :
#     print("짝수 입니다")

#  사용자로부터 입력받은 시간이 정각인지 판별하라.
# time  = input("현재시간 : ")

# #  실행 예
# #  현재시간 (입력예시 3 : 05) >> 5 :20
# #  정각이 아닙니다.

# if time[-2:] != "00" :
#     print("정각이 아닙니다.")
# else :
#     print("정각입니다.")

#  점수구간 학점
#  사용자로부터 score를 입력받고 학점출력

# score = int(input("점수를 입력해주세요 : "))
# if 100 >= score >= 81 :
#     print('A학점입니다.')
# elif score >= 61 :
#     print('B학점입니다.')
# elif score >= 41 :
#     print('C학점입니다.')
# elif score >= 21 :
#     print('D학점입니다.')
# elif 0 <= score < 20 :
#     print('E학점입니다.')
# else :
#     print('잘못된 입력입니다.')


#  사용자로부터 세 개의 숫자를
#  입력 받은 후 가장 큰 숫자를 출력하라.

# 출력 예시
# >>input number1 : 10
# >>input number2 : 9
# >>input number3 : 20

num1 = int(input(">>>input number1 :"))
num2 = int(input(">>>input number2 :"))
num3 = int(input(">>>input number3 :"))

if num1 >= num2 and num1 >= num3 :
    print(num1)
elif num2 >= num1 and num2 >= num3 :
    print(num2)
elif num3 >= num1 and num3 >= num2 :
    print(num3)

