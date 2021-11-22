#  for 문이용해서 구구단 만들기
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i * j}")
    print("\t")

#  평균성적을 구하고 80점이상이면 합격 출력
#  80점 미만은 불합격 입니다. 출력

scores = [90, 100, 87 , 89, 82]

total  = 0
avg = 0

for i in scores:
    total += i

avg = total/len(scores)

if (avg >= 80):
    print("합격입니다")
else:
    print("불합격입니다")
