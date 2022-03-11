import xlrd
book = xlrd.open_workbook('stu.xlsx') #打开一个excel
sheet = book.sheet_by_index(0)       #根据顺序获取sheet
sheet2 = book.sheet_by_name('sheet1')  #根据sheet页名字获取sheet
# print(sheet.cell(0,0).value)  #指定行和列获取数据
# print(sheet.cell(0,1).value)
# print(sheet.cell(0,2).value)
# print(sheet.cell(0,3).value)
# print(sheet.ncols) #获取excel里面有多少列
# print(sheet.nrows) #获取excel里面有多少行

# for i in sheet.get_rows():
#     print(i)

for i in range(sheet.nrows):
    print(sheet.row_values(i))#获取几行的数据

print(sheet.col_values()) #取第几列的数据  （）里面填数字