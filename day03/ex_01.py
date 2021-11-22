# 커피 1잔을 300원에 판매하는 커피 자판기
#  이커피 자판기에 돈넣으면 자판기에서 뽑을 수 있는 커피가 몇잔이며 , 잔돈은 얼마인지 출력하는 프로그램
#  실행 예
#  자판기에 얼마를 넣을까요 ? >>\
#  커피 1잔, 잔돈 1100원 
#  커피 2잔 잔돈 800원
#  잔돈 200원 반환
coffee = 0
insert_money = int(input("자판기에 얼마를 넣을까요 ? >>>>"))

while insert_money >= 300 :
    coffee += 1
    insert_money -= 300
    print(f"커피 {coffee}잔,잔돈 {insert_money}원")
