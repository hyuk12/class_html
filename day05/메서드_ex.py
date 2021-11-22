# 전화번호 입력받고 뒷번호 네자리 출력

# tel = input("전화번호 입력해주세요")

# print(f"뒷 번호는 :{tel.split('-')[2]}")

#  전번 입력받고 '-' 빼고

# telNum = input("전화번호 입력하세요 : ")
# print(f"전화번호는 {telNum.replace('-','') } 입니다.")

# 앤드를 입력할때까지 데이터 입력
#  입력받은 데이터가 정수형태의 값만 더하고 출력

list = []
sum = 0
while True :
    num = (input("숫자입력 : "))
    list.append(num)
    if num.isdecimal() == True :
        sum += int(num)
    if num == "end" :
        break
print(sum)
