# numbers = [0,1,2,3,4,5,6,7,8,9]

# i  = 0
# for sum in numbers:
#    i = sum + i
# print(i)

# 월드컵은 4년에 한번 개최된다.
#  range()사용
#  2002 년~ 2050년

# for i in range(2002,2051,4):
#     print(i)

# 아래와 같이 리스트의 데이터를 출력하라.


# price_list = [32100, 32150, 32000, 32500, 321010]

# for i,v in enumerate(price_list):
#     print(i ,v)

# for i in range(len(price_list)):
#     print(len(price_list) - i,price_list[i])

#  구구단 3단 출력 단 홀수 번째만 출력

# for i in range(1,10,2):
#     print(f"{3} * {i} = {3 * i}")

for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i * j}")
    print("\t")

#  사용자로부터 숫자 입력받고
#  1부터 입력받은 숫자까지의 합을 구하는 프로그램 구현

#  1부터 얼마까지 더해볼까요 ? 10
#  1ㅂ  ㅜ터 10까지 정수의 합은 55 입니다.

# num = int(input("1부터 얼마까지 더해볼까요? : "))
# sum = 0
# for i in range(num):
#     i += 1
#     sum += i
# print (f"1 부터 {num} 까지 정수의 합은 {sum} 입니다.")

#  my list 를 아래와 같이 출력하라
#  가나
#  나다
#  다라

# my_list = ['가','나','다','라','마']

# # for i in range(len(my_list) - 2):
# #     print(my_list[i], my_list[i+1], my_list[i+2])

# for i in my_list[::-1]:
#    print(i)

