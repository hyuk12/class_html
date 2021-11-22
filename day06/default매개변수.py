# default매개변수 
# 기본값을 정해주는 매개변수 인수에 자리할 때 디폴트 매개변수가 앞에 올 수 없다.
#  금액과 세금입력 받으면
#  해당금액에서 세금액을 반환하는 메서드 작성
#  만약 세금을 입력하지 않으면 0.1로 계산하시오

def taxCal(money,tax = 0.1):
    tax_money  = int(money * tax) 
    print(f"세금은 {tax_money} 원 입니다.")

taxCal(10000,0.05)
taxCal(10000)