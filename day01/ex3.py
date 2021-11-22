# 5자리로 구성된 학번이 있습니다
# 31025
# 3학년 10반 25번
# 정수형
student_num = 31025
#-----------코드
a = str(student_num)[:1]  
b = str(student_num)[1:3]
c = str(student_num)[3:]
# print(a)
print(a + "학년 " + b + "반 " + c + "번")
# 3학년 10반 25번

# 차량 번호에서 뒤에 숫자4자리만 출력하는
# 프로그램 
# 차량번호는 '부산29우1234' '10가 3456' '234마9876'

car1 = '부산29우1234'
car2 = '10가3456'
car3 = '234마9876'

carName1 = car1[:5]
carName2 = car2[:3]
carName3 = car3[:4]

carNum1 = car1[5:]
carNum2 = car2[3:]
carNum3 = car3[4:]

print(carName1 + " 의 차량번호 4자리는 " + carNum1 + "입니다.")
print(carName2 + " 의 차량번호 4자리는 " + carNum2 + "입니다.")
print(carName3 + " 의 차량번호 4자리는 " + carNum3 + "입니다.")
