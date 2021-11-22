#  가변 매개변수
#  매개변수를 받을 때 앞에 *(애스터리스크)을 붙여준다 갯수를 정하지 않고 쓰는 매개변수
#  시퀀스 로 전달되는데 튜플로 전달된다. (수정불가)

#  가변 매개변수로 정수혹은 실수 입력하면
#  입력받은 매개변수의 총 합을 반환하는 함수 작성

# def my_sum(*number):
#     sum = 0
#     for i in number:
#         sum += i
#     return sum
# n =  my_sum(4,6,5.9)
# m =  my_sum(9, 7.4, 5.9)
# o =  my_sum(4.7,6.9,5.9)

# print(n)
# print(m)
# print(o)

#  리스트 입력 받으면 
#  총합, 평균, 최댓값, 최소값을 반환하는 함수 작성

def func (list):
    x,y,z = sum(list) , max(list), min(list)
    avg = sum(list)/len(list)
    print(f"{x} , {y}, {z},{avg}")

func([1,2,3,4,5])
