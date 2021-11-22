# 클래스
#  객체 object
# 실제로 존재하는 모든 것 :사물이나 개념
# 용도 : 객체가 가지고 있는 기능과 속성에 따라 다르다
# 유형의 객체 : 책상, 의자, 자동차, 티비/....
# 무형의 객체: 수학공식, 프로그램에러, 논리개념

#  클래스
# 객체를 정의해 놓은 것
# 자료형을 위한 템플릿
#  어떤정보도 담을 수 있고, 자료형과 어떻게 상호작용 하는지 적어두고 쓰는 것

#  자료형(type)
#  클래스 정의
# 1 . class 라는 키워드 써서 정의
# 2 . upper camel case

# class MyClass():
#     pass
# # 인스턴스 생성
# # 객체 생성과 같은 말
# #  객체  = 클래스()

# object1 = MyClass()
# object2 = MyClass()
# print(type(object1))

# 클래스의 구성
# 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수
# 메서드 : 클래스 내에서 생성할 때 ()안에 self를 넣어준다.
# 인스턴스변수
# 인스턴스메서드

# 사람이라는 클래스를 만들고 객체생성하고 클래스가 만들어 지면 cry()라는 메서드를 만들어서 실행해보세요

# class Human():
#     def cry(self, name, call):

#         return print(name + "에게 " + call + " 발신중")


# human = Human()
# human.cry("김철수", "010-1234-5678")
# 구구단 클래스

class Gugu():
    def multiple(self, number):
        i = 1
        while i < 10:
            print(f"{number} * {i} = {number * i}")
            i += 1


m = Gugu()
m.multiple(3)
