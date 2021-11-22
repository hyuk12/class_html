#  평균 성적 구하고 80점 이상이면 합격 출력
#  80점 미만은 불합격 출력

# scores = [90, 100, 87, 89, 82, 10]
# total = 0

# for i in scores:
#     total += i

# avg = total / len(scores)

# if avg >= 80 :
#     print(f"평균성적은 {avg}점으로 합격입니다.")
# else:
#     print(f"평균성적은 {avg}점으로 불합격입니다.")

#  숫자 퀴즈!
#  up and down 퀴즈

import random

number = random.randint(1,100)
count = 0
print(number)
input_num = int(input("1부터 99까지 숫자를 맞춰보세요. : "))
while True:
    count += 1
    if input_num > number:
        print("틀렸습니다.")
        input_num = int(input("더 낮은 수를 입력하세요"))
    elif input_num < number:
        print("틀렸습니다.")
        input_num = int(input("더 높은 수를 입력하세요"))
    else:
        print("정답입니다.")
        break
print(f"당신은  {count}회만에 맞추셧습니다.")