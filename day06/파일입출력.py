# 파일 입출력
# 파일 쓰기
# file = open('text.txt', 'wt', encoding = 'utf8')
# file.write("Hello World!")
# file.close()
# # 파일 읽기
# file = open('text.txt', 'rt', encoding = 'utf8')
# contents = file.read()
# print(contents)
# file.close()

# #  파일추가
# file = open('text.txt' , 'at', encoding='utf8')
# file.write("\n고생하십니다.")
# file.close()

# file = open('text.txt', 'rt', encoding = 'utf8')
# contents = file.read()
# print(contents)
# file.close()

# score = [['홍길동', 100, 80, 60],["김철수", 40, 40, 80]]
# text = ''

# for item in score:
#     for i in item:
#         text = text + str(i) + ','
#     text = "\n"

# file = open('score.txt', 'wt' , encoding='utf8')
# file.write(text)
# file.close()

item = [["005930 삼성전자\n"],["005380 현대차\n"],["035420 NAVER"]]

for i in item:
    item_box = []
    item_box += str(i)



file = open("매수종목1.txt", "wt", encoding="utf8")
file.write(item_box)
# file.write("005930 삼성전자\n"  "005380 현대차\n"  "035420 NAVER")
file.close()