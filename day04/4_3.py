#  continue /  break
#  continue  : 이번조건은 스킵
#  break  : 조건문 전체 중단하고 탈출
#  순서대로 불러서 책을 읽자
#  결석한 학생은 넘어가겠습니다.
#  딕셔너리 for문은 .items붙인다.

absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"자습해라 {student}번은 교무실로...")
        break
    print(f"{student}번 일어서서 책읽어!")

total = 0
i = 0
while True:
    if i > 10:
        break
    total += i
    i += 1
print(total)