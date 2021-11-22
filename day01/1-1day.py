# 문자열 인덱싱(string indexing)

# index : 문자열을 구성하는 모든 문자에 부여된 고유번호
# 메모리 번호
# 시작번호가 0

s = 'hello'
print(s[::-1])

# letters가 바인딩하는 문자열에서 세번째 문자를 출력하세요
str = "letters"
letters = "python"
print(str[2])
print(str[-5])
print(letters[2])
print(letters[-4])

# y o
print(letters[1],letters[-2])

#  문자열 슬라이싱 string slicing
#  문자열을 잘라내는 것


# s[시작값: 종료값 : 증감값]
# s[start :end : step]
s = 'python'
# 증감값을 생략하면 1
print(s[0:2])
print(s[1:3])
# 초기값을 생략하면 0
print(s[:3])
# 종료값을 생략하면 끝까지 
print(s[3:])
alpha = 'abcdefghijklmn'
print(alpha[::2])