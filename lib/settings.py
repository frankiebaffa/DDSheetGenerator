import xlwt

def init():
    global book
    book = xlwt.Workbook(encoding = "utf-8")

    global sheet
    sheet = book.add_sheet("Sheet 1", cell_overwrite_ok=True)
