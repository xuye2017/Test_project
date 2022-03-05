import  pymysql
'''
1、连接上mysql IP 端口号 密码 账号 数据库
2、建立游标
3、执行sql
4、获取结果
5、关闭链接、关闭游标
'''

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='112233',port=3306,db='infotest',charset='utf8')
cur = conn.cursor()  #建立游标，游标就当做是仓库管理员
cur.execute('show tables;') #执行sql语句，select insert delect update
conn.commit()#t提交
res = cur.fetchall()#获取sql语句执行的结果，它把结果放在一个元组里，每一条数据也是一个元组
#res = cur.fetchone()#只获取一条结果，它的结果是一个1维元组
print(res)
print('fetchall',cur.fetchall())
# cur.scroll(0,mode='absolute') #移动游标，到最前面
# cur.scroll(-10,mode='relative') #移动游标，到相对当前位置
# print('fetchone'cur.fetchone())
# cur.close()#关闭游标
conn.close()#关闭连接