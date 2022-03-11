import xlwt
# book =xlwt.Workbook()#新建一个excel
# sheet = book.add_sheet('sheet1') #添加一个sheet页
# sheet.write(0,0,'姓名')
# sheet.write(0,1,'性别')
# sheet.write(0,2,'年龄')
# book.save('stu.xlsx')

title =['姓名','年龄','性别','分数']
stus =[['mary',20,'女','89.9'],
       ['mary',20,'女','89.9'],
       ['mary',20,'女','89.9'],
       ['mary',20,'女','89.9']]

wbk =xlwt.Workbook()
sheet = wbk.add_sheet('sheet1')
cols =0

for t in title:
    sheet.write(0,cols,t)
    cols+=1

row =1  #控制行
for stu in stus:
    new_col = 0  # 控制列
    for s in stu:  #写每一列的
        sheet.write(row,new_col,s)
        new_col+=1
    row+=1
wbk.save('stu.xlsx')

# for i in range(len(title)):
#      sheet.write(0,i,(title)):#写入表头


# for i in range(len(stus)):
#     if i !=0: #如果不是表头的话
#         for j in range(4):
#             sheet.write(i,j,stus[i][j])#循环写入每行数据
#
# #保存数据到‘test。xls’文件中
# wbk.save('szz.xls')