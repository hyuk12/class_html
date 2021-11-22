# 문자열 연산 더하기 곱하기
# 문자열은 더하면 붙어버린다
# 문자열 곱하기는 숫자만큼 복사

a = "hello"
b = "world"
print(a*5)
# 화면에 * 35개 연산자 이용해서 출력하기

print("*\t" * 35)
# letters 가 바인딩 하는 문자열에서 덧셈 연산을 이용해 첫번째와 세번째 문자를 출력하세요

letters = 'python'
a = letters[0]
b = letters[2]
print(a + b)

# 나는 python을 공부합니다
print("나는 " + letters + "을 공부합니다.")

a = 1
b = "2"
print(str(a) + b)