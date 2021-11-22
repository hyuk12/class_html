# 0 을입력받을때까지 정수입력받기
list = []

while (True) :
    num = (int(input("정수 입력해주세요")))
    if (num == 0):
        break
    list.append(num)

print(f"총합 : {abs(sum(list))} ")
print(f"평균 : {round(abs(sum(list)/len(list)), 2)}  ")
print(f"최대값 : {max(list)} ")
print(f"최소값 : {min(list)} ")