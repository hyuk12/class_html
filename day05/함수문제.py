#  성적 리스트 입력받아서
#  평균을 출력하는 print_score 함수 정의

# list = [1,2,3,4,5]

# def print_score(listrandom):
#     avg  = sum(listrandom)/len(listrandom)
#     return print(f"평균은 {avg}점 입니다.")

# print_score(list)

#  하나의 리스트를 받아
# 짝수만 화면에 출력하는 print_even 함수 정의

# num = [1, 3, 2, 10, 12, 11, 15]

# def print_even(list):
#     for i in list:
#         if(i % 2 == 0):
#             print(i)
# print(f"{list}")

# print_even(num)

# 연봉 입력받아 월급계산
# calc_monthly_salary(annual_salary)
#  함수 정의
#  회사 연봉 12개월 나누어 분할지급
# def calc_monthly_salary():
#     money = int(input("연봉을 입력"))
#     annual_salary = int(money / 12)
#     print(f"월급은 {annual_salary} 만원 입니다.")

# calc_monthly_salary()

#  값두개 입력받아서
#  합과 곱을 구하는 함수 만들기

# 700원 짜리 음료수 자판기
#  돈넣으면 몇잔의 음료수 뽑을수있는지
# 잔돈은 얼마인지 모든경우의수

def vending_machine():
    price = 700
    insert_money = int(input("돈을 넣어주세요"))
    count = int(input("몇개를 뽑을까요"))
    money = insert_money - (price * count) 
    
    print(f"음료수 = {count}개 , 잔돈 ={money}  ")

vending_machine()


# devdol.com/python-today