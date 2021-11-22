 # 복습
#  컬렉션 4종
# 리스트, 튜플, 세트, 딕셔너리
#  리스트 []
#  여러가지 값을 저장할 때 사용한다
#  데이터 형식이 다르더라도 하나의 리스트 작성 가능
# 리스트  = [값, 값, 값]
#  순서가 있어서 인덱싱, 인덱싱 슬라이싱이 가능하다

# 추가 수정 삭제가 가능

#  추가 : append(), insert
#  삭제 : pop(삭제할 인덱스), remove()
#  수정 : 리스트 [인덱스] = 수정할 값

list = ["아이유" , 29, 164.5, False]

list.append("edam")
print(list)

list.insert(1, "Female")
print(list)

list.pop()
print(list)

list.pop(1)
print(list)

#  정렬
#  sort(), reverse()
# 찾기 읽기
# index(위치를 찾을 값) - 입력한 값은 인덱스를 반환
# count(카운트할 값) - 입력한 값이 몇개 있는지 알려줌

# len() - 리스트 길이
len(list)

#  튜플 : 소괄호 (값, 값)
#  저장된 값을 변경 할 수 없다.
#  인덱싱 슬라이싱 가능하다.

#  세트 : 중괄호 {값,값,값}
#  수학의 집합과 유사한 개념
#  중복이 안되는 특징
#  순서가 없어서 슬라이싱 인덱싱 불가
#  new_set = { } 하면안됨

set = {1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,}
print(set)

#  딕셔너리
#  {키 : 값, 키 : 값, 키 : 값, 키 : 값}

#  input() 은 str 산술적으로 계산하려면 int형변환


# python 의 첫번째 문자와 세번째 문자 출력

value1 = "python"
print(value1[0:1])
print(value1[2:3])
value = ["PYTHON"]
print(value[0][0],value[0][2])

print("\"C:\\Windows\"")
#  화면에 "ㅋ" 30번
val = "ㅋ"
print(val * 30)

