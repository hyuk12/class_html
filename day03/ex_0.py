# days = [31,28,31,30,31,30,31,31,30,31,30,31]
# 1~12 까지 값을 입력받아
# 해당월은 몇일 까지 있는지 출력해봅시다
# 실행 예)
#  몇월의 날짜수가 궁금하세요?
# 2월은 28일 까지 있습니다

# month_input = int(input("몇 월의 날짜 수가 궁금하세요? :"))

# print(f"{month_input}월은 {days[month_input-1]}일 까지 있습니다.")

#  주차장에 60대로 주차 대수가 정해져있다.
#  차량이 들어오는 대수를 입력받으면
#  남은 주차대수를 구하는 프로그램을 작성하시오

#  실행 ㅇㅖ
#  주차된 차량댓수 : 20
#  남은 주차장 자리는 40
# limit = 60
# incar = int(input("들어오는 차량수 입력 : "))
# empty = limit - incar
# if limit > incar : {
#     print(f"주차된 차량 댓수 : {incar} \n남은 주차장 자리는 {empty}개 입니다. ")
# }
# else : {
#     print("주차 공간이 없습니다.")
# }

#  임의의 두자리 정수 (10~99)를 입력 받아서
#  십의 자리와 일의자리로 분리하여
#  출력하는 프로그램을 구현하시오.

#  실행예 
#  임의의 두자리 정수를 입력하세요
#  십의자리 : 5
#  일의자리 : 3

# random_integer = int(input("임의의 세자리 정수를 입력하세요 : "))

# front_num = (random_integer // 100)
# middle_num = (random_integer // 10 % 10 )
# back_num = random_integer % 10
# print(f"100의 자리 : {front_num} \n10의 자리 : {middle_num} \n1의 자리 : {back_num}")

#  1분은 60초, 1시간은 60분일때,
#  임의의 초를 입력받아 해당 초를
#  시, 분 , 초로 변환하여 출력하는 프로그램 구현

# 실행 예
#  초를 입력하세요 :
#  1시간 0분 0초 입니다.

# sec = int(input("초를 입력해주세요 : "))

# time = sec // 3600
# min =  (sec // 60)%10
# sec2 = sec % 60
# print(f"{sec}는 {time}시 {min}분 {sec2}초 입니다.")

#  수학여행을 어디로 갈지 결정하기 위한 설문조사
#  학생들이 원하는 장소를 입력받아 동일한 입력은 무시하고
#  모든입력을 저장
#  학생을 3명으로 가정하고 프로그램
#  실행 예

#  희망하는 여행지를 입력하세요 >>>

#  조사한 여행지는{"제주", "부산"}

# s = set()
# s.add(input("희망하는 여행지를 입력하세요 >>>"))
# s.add(input("희망하는 여행지를 입력하세요 >>>"))
# s.add(input("희망하는 여행지를 입력하세요 >>>"))

# print(f"조사한 여행지는 {s}")

#  파이썬 영어사전
#  딕셔너리 생성
#  영어단어 입력하면 뜻출력

eng_dict = {
    "flower" : "꽃",
    "fly" : "날다",
    "floor" : "바닥",
}
word = input("단어 입력해주세요 : ")
meaning = eng_dict.get(word)
print(f"{word}의 뜻은 {meaning}")