import pymysql,redis
from conf import setting
def op_mysql(sql):
	conn = pymysql.connect(host=setting.MYSQL_HOST,user=setting.USER,
						   password=setting.PASSWORD,
						   port=setting.PORT,
						   charset='utf8',db=setting.DB)
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

def op_redis(host,password,k,v=None,port=6379,db=0):
	r = redis.Redis(host=host,password=password,port=port,db=db)
	if v:
		r.set(k,v)
		res = 'ok'
	else:
		res = r.get(k)
		if res: #这里是判断有没有get到数据
			res = res.decode()
		else:
			res = None
	return res

# print(__name__)
# print('哈哈哈哈，我在这里头')
if __name__=='__main__':
	#别人导入这个python文件的时候，下面的代码不会被执行
	#自己测试的时候用
	# print(__name__)  # __main__
	# print('哈哈哈哈哈哈 到底有没有执行')
	sql = 'select * from bt_stu limit 5;'
	sql2 = 'update bt_stu set class="天蝎座3" where id=503;'
	res = op_mysql(
		host='211.149.218.16',
		user='jxz',password='123456',#port这里一定要写int类型
		port=3306,db='jxz',charset='utf8',sql=sql2)
	print(res)