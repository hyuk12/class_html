#  for 문
#  반복할 횟수가 정해져 있을 때 사용
#  while 문보다 훨씬 자주 씁니다,.

#  for 변수 in 반복가능한 객체 :
#  반복할 실행문

#  반복가능한 객체 : 시퀀스 자료형 - 순서를 가지는 객체 list tupel 문자열 , range
#  비시퀀스  : 순서가 없는 객체 - set , dict
#  for 없이 변수 in 리스트 로 조건문이 가능하다

# li = ["b1","1층","2층","3층","4층"]

# for i in li:
#     print(f"현재 {i}층 입니다.")

#  for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.

# list = ["김밥","라면","튀김"]

# # 오늘의 메뉴

# for i in list:
#     print(f"오늘의 메뉴 : {i}")

#  리스트에 주식 종목이름이 저장되어있다.
#  for문을 사용해서 저장된 문자열의 길이를 다음과 같이 출력하라.

# list = ["SK하이닉스","삼성전자","LG전자"]

# for i in list:
#     print(len(i))

#  if 문과 for문을 사용해서 리스트에서 음수 출력

# list = [3, -20, -3, 44, 12, 21]
# # for num in list:
# #     if num < 0 :
# #         print(num)

# # for num in list:
# #     if num % 3 == 0 :
# #         print(num)

# for num in list:
#     if num % 3 == 0 and num < 20 :
#         print(num)
               
#  리스트에서 세글자이상의 문자를 화면에 출력하라
# list  = ["I","study","python","language","!"]

# for i in list :
#     if len(i) >= 3:
#         print(i)

# #  인덱스 번호랑 값이랑 같이 출력하기
# # enumerate
# a = [38, 21, 53, 62, 19]

# for index, value in enumerate(a):
#     print(index,value)

# #  인덱스 번호를 원하는 숫자부터 출력하기

# for index, value in enumerate(a,start=10):
#     print(index,value)

#  range() 함수는 범위를 생성
#  range(초기값, 종료값, 증감값)
#  range(10) : 0~ 10까지
#  range(5, 10) : 5~ 10까지
#  range(2, 10, 2) : 2 4 6 8

#  for 문 

for i in range(0,1000):
    print(i)
