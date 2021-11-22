#  중간고사 성적발표
#  한반에 8명 학생
#  각학생의 국어점수 번호순 나열
# exam = [99, 78, 100, 91, 54, 100, 71, 50]

# # 마음착한선생이 모든학생점수 5점씩올려주기로 함
# #  5점씩 올린 score 리스트 출력
# #  단, 100점 초과 하면안됨

# score = []
# for i in exam:
#     if i + 5 > 100:
#         score.append(100)
#     else:
#         score.append(i + 5)
# print(score)