import pymysql
def op_mysql(host,user,password,db,sql,port=3306,charset='utf8'):
	conn = pymysql.connect(host=host,user=user,
						   password=password,
						   port=port,
						   charset=charset,db=db)
	cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
	cur.execute(sql)
	sql_start = sql[:6].upper() #取sql前6个字符串，判断它是什么类型的sql语句
	if sql_start=='SELECT' :
		res = cur.fetchall()
	else:
		conn.commit()
		res = 'ok'
	cur.close()
	conn.close()
	return res

# conn = pymysql.connect(host='211.149.218.16',user='jxz',
# 					   password='123456',
# 					   port=3306,
# 					   charset='utf8',db='jxz')
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
# name='zdq'
# # sql = 'select * from bt_stu where username="%s"; '%name
# sex='nv'
# cur.execute('select * from bt_stu where real_name="%s;"' % name) #可以sql注入的
# cur.execute('select * from bt_stu where real_name=%s and sex = %s',(name,sex)) #可以防止sql注入
# print(cur.fetchall())


def test(a,b):
	# print(a,b)
	pass
li = [1,2]
d = {'a':'ybq','b':'mpp'}
test(*li)
test(**d)
conn = pymysql.connect(host='211.149.218.16',user='jxz',
					   password='123456',
					   port=3306,
					   charset='utf8',db='jxz')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

def op_mysql_new(sql,*data):
	#利用 *data这个可变参数，就能防止sql注入了
	print(sql)
	print(data)
	cur.execute(sql,data)
	# cur.execute('select',(name,id,name))
	# cur.execute('select * from user where name=%s',('haha'))
	print(cur.fetchall())
# sql = 'select * from user where username  = %s and sex=%s;'
# name='haha'
# sex='xxx'
# op_mysql_new(sql,name,sex)

conn = pymysql.connect(host='211.149.218.16',user='jxz',
					   password='123456',
					   port=3306,
					   charset='utf8',db='jxz')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = 'insert into seq (blue,red,date) values (%s,%s,%s)'
all_res = [
	['16','01,02,03,05,09,06','2018-01-28'],
	['15','01,02,03,05,09,06','2018-01-28'],
	['14','01,02,03,05,09,06','2018-01-28'],
	['13','01,02,03,05,09,06','2018-01-28'],
	['13','01,02,03,05,09,06','2018-01-28'],
	['13','01,02,03,05,09,06','2018-01-28'],
	['13','01,02,03,05,09,06','2018-01-28'],
	['13','01,02,03,05,09,06','2018-01-28'],
	['13','01,02,03,05,09,06','2018-01-28'],
	['13','01,02,03,05,09,06','2018-01-28'],
	['13','01,02,03,05,09,06','2018-01-28'],
	['13','01,02,03,05,09,06','2018-01-28'],
]
cur.executemany(sql,all_res) #执行多个条件的。。
conn.commit()