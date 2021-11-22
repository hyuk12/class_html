# secure_name(): 이름의 성만 남기고 *로변환
# secure_jumin():주민번호의 성별 식별번호까지만 남기고 * 변환
# secure_phone():전화번호의 국번을 *로 변환

def secure_name(name):

    return name[0] + "**"


def secure_jumin(juminNumber):
    return juminNumber[0:8] + "******"


def secure_phone(number):
    return number[0:4] + "****" + number[-5:]
