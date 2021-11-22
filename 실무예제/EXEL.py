import xlsxwriter

workbook = xlsxwriter.Workbook("20211121.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write("A1", "test")
workbook.close()
