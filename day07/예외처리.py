# 고전적인 예외처리


# try:
#     a = int(input("나눠질 값을 입력하세요: "))
#     b = int(input("나눌 값을 입력하세요: "))
#     print(f"{a} / {b} = {a / b}입니다.")
# except:
#     print("처리 할 수 없습니다.")
# PER = ["10.31", "", "8.00"]

# for i in PER:
#     try:
#         print(float(i))
#     except:
#         print(0)
#  특정 예외만 처리하는 방식

try:
    a = int(input("나눠질 값을 입력하세요: "))
    b = int(input("나눌 값을 입력하세요: "))
    result = a/b
except ZeroDivisionError:
    print("0으로 나눌수 없습니다")
except ValueError:
    print("정수가 아닙니다")
except Exception:
    print("알 수 없는 에러")
else:
    print(f"{a} / {b} = {result}입니다.")
finally:
    print("종료")
