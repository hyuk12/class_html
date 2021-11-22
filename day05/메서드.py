# 메서드
#  객체.메서드
#  .append() , .pop() ...
#  split()
# 하나의 문자열을 여러개로 분리해서 리스트로 반환

#  기본적으로는 공백을 기준으로 분리
#  특정문자열로 분리 할수도 있다.

address = "부산 광역시 해운대구 좌동 123"
print(address.split())

# strip()
# 양쪽 끝에 있는 공백 제거하고 리턴

# replace()
#  일부문자를 다른 문자로 변환하여 반환

str = "My name is Ironman"
new_str = str.replace("Ironman", "Hulk")
print(new_str)

# isdecimal 정수형인지 아닌지 구분
#  boolean 타입

str1 = "1234"
str2 = "good"
print(str1.isdecimal())
print(str2.isdecimal())

# count("찾을 문자열", 시작위치, 끝위치)