try:
    filename = input("열고자 하는 파일명을 입력하세요.")
    file = open(filename, 'rt', encoding='utf8')
except FileNotFoundError as e:
    print(f"에러내용 : {e}")
else:
    buffer = file.read()
    print(buffer)
finally:
    file.close()
    print("읽음 끝")
