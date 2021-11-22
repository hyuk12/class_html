# 웹크롤링
#  webp상에서 존재하는 컨텐츠를 수집하는 작업 >크롤링
# requests
# beautifulsoup
# xlsxwriter
import requests
# requests 라이브러리
import bs4
import xlsxwriter

workbook = xlsxwriter.Workbook("20211119.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write("A1", "시총순위")
worksheet.write("B1", "종목명")
worksheet.write("C1", "현재가격")


def return_value(address):
    res = requests.get(address)
    res.encoding = "UTF-8"
    soup = bs4.BeautifulSoup(res.content, "html.parser")

    section = soup.find('tbody')
    items = section.find_all("tr", onmouseover="mouseOver(this)")

    for item in items:
        basic_info = item.get_text()
        sinfo = basic_info.split("\n")
        worksheet.write(int(sinfo[1]), 0, sinfo[1])
        worksheet.write(int(sinfo[1]), 1, sinfo[2])
        worksheet.write(int(sinfo[1]), 2, sinfo[3])
        # print(sinfo[1] + "\t\t" + sinfo[2] + "\t\t\t" + sinfo[3])


base_address = "https://finance.naver.com/sise/sise_market_sum.naver?page=1"

for i in range(1, 5):
    return_value(base_address + str(i))
# url = 주소(https:// 주소값/ 세부주소?속성=값&속성=값)
workbook.close()
