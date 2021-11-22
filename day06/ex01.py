# 나라별 수도를 순차적으로 반복시켜서
# nation 리스트에 저장해 두었다
# 내용을 이용하여 다음과같은
# nation.txt 파일을 만들어보세요

# nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국','워싱턴']

# file = open('nation.txt', 'wt' , encoding='utf8')
# for i,j in enumerate(nation):
#     if i % 2 == 0:
#         file.write(j)
#     else:
#         file.write(" - " + j + "\n")
   

# file.close()

#  1부터 10000000 까지의 합계 구하고 그결과와 연산에 걸린 시간을 출력


import datetime
t1 = datetime.datetime.now()
num = 0
for i in range(10000000):
    
    num += i
    

t2 = datetime.datetime.now()
print(num)
print(t2 - t1)