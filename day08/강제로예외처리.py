# 강제로 예외처리
# raise
#  점수 입력받고 점수가 80점이상 합격
# 80점이하면 불합격
# 음수나 100점이상입력할때
# 0~100점사이를 입력하라고한다

# score = int(input("점수를 입력하세요: "))
# try:
#     if score < 0 or score > 100:
#         raise Exception("점수는 0~100점사이를 입력하라")
# except Exception as e:
#     print(e)
# else:
#     if score >= 80:
#         print(f"{score}은 합격")
#     else:
#         print(f"{score}은 불합격")

#  사용자 정의 오류 발생시키기
# Exception 클래스 상송받아서 발생

# class MyError(Exception):
#     def __init__(self):
#         super().__init__("사용자 에러 발생")


# class HourError(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)


# hour = int(input("시간을 입력하세요: "))
# try:
#     if hour < 0 or hour > 23:
#         raise HourError("올바른 시간이 아닙니다")
# except HourError as e:
#     print(e)

class NameError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


name = input("이름을 입력해주세요.(2~6글자사이) >>")
try:
    if len(name) < 2 or len(name) > 6:
        raise NameError("글자수가 알맞지 않습니다.")
except NameError as e:
    print(e)
else:
    print(f"입력된 이름은 {name}입니다.")
finally:
    print("프로그램 종료")
