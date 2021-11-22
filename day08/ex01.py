# 다음 지시사항읽고 생성한 난수를 맞히는 updown 게임실행
# updown 클래스구현
#  지시사항
#  클래스 인스턴스를 생성하면 1~100사이의 난수가 변수 answer 에 저장
# 인스턴스 생성후에는 play()메소드만 호출
# game = updown()
# game.play()
# challenge( 메서드는 사용자의 입력을 처리
# 유효하지 않은 정수값을 입력하면 예외처리
# 1~100까지 값만 입력
# 첼린지가 호출될 때마다 count가 1씩 증가
# 최종적으로 count 변수값으로 몇번의 시도 끝에 성공했는지 알수 있다
# 생성된 난수를 맞히기전에는 프로그램이 종료되지 않는다
# 정수대신 다른 자료형의 값은 입력되지않는다고 가정
#
#
import random


class UpDown():
    def __init__(self):
        self.answer = random.randint(1, 100)
        self.count = 0

    def challenge(self):
        self.count += 1
        a = int(input("맞출 숫자를 입력해주세요: "))
        if a < 1 or a > 100:
            raise Exception("숫자범위에서 벗어났습니다.")
        return a

    def play(self):

        print(self.answer)

        while True:
            try:
                res = self.challenge()
            except Exception as e:
                print(e)
            if self.answer < res:
                print("down")
            elif self.answer > res:
                print("up")

            else:
                print(f"{self.count}번 시도만에 찾았습니다.")
                break


game = UpDown()
game.play()
