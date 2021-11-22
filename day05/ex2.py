# 쉼표 구분 문자열형식 학생이름과 성적 입력
#  이데이터 각각 name과 score변수에 저장하는 프로그램

student = '"김철수" , 85'

name = student.split(',')[0].strip('"')
score = student.split(',')[1]

print(f"이름은 {name}이고, 점수는{score}점 입니다")