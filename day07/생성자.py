# 클래스 변수 인스턴스 변수 함께사용

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# man = Person("홍길동", 30)
# print(man.name, man.age)

# class Human():
#     def __init__(self, name):

#         print(f"{name} 님이 태어났습니다")


# human = Human("유종훈")
# human1 = Human("조현호")

class FootBallPlayer():
    def __init__(self, name, age, team, nation, position):
        self.name = name
        self.age = age
        self.team = team
        self.nation = nation
        self.position = position


son = FootBallPlayer("손흥민", "30살", "토트넘", "대한민국", "공격수")
print(son.name, son.team)
