#  성별과 키를 이용해서 표준체중 만드는 프로그램
#  남자 : 키(m) * 키(m) *22
#  여자 : 키 곱 키 곱 21
#  표준체중은 별도의 함수내에서 ㄱ/산

#  standard_weight
#  gender전달값 , height키값
#  표준 체중은 소수점 둘ㅉㅐ자리까지

# def standard_weight(gender, height):
#     if gender == "남자":
#         man_weight = height * height * 22 / 10000
#         print(f"키 {height}cm {gender}의 표준체중은 {man_weight:.2f}")
#     elif gender == "여자":
#        women_weight = height * height * 21 / 10000
#        print(f"키 {height}cm {gender}의 표준체중은 {women_weight:.2f}")
#     else:
#         print("잘 못 입력 하셨습니다.")

# standard_weight("남자",170)
# standard_weight("여자",167)
#  어제 복습임
# key가 과목명 value 가 점수 marks 딕셔너리
#  전달하면 해당 딕셔너리에 저장된 ㅎ점수들의 평균을 반환하는 get_average()함수구현

# 함수정의
# 반환값 : 평균
# 매개변수 : 딕셔너리 marks

marks = {
    "국어":90,
    "영어":80,
    "수학":85
}

def get_average(marks):
    for i in marks:
        score = marks[i]
        sum = score + score
    avg = sum/len(i)
    return avg
avg = get_average(marks)
print(f"평균은 {avg} 입니다.")
