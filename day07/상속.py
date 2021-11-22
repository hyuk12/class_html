class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}이 밥을 먹습니다")


class Student(Person):
    def __init__(self, name, age, school, grade):
        super().__init__(name, age)
        self.school = school
        self.garde = grade

    def study(self):
        print(f"{self.name}이/가 {self.school}에서 공부합니다.")


man = Student("홍길동", 26, "서울대", "3학년")
man.study()
man.eat()
