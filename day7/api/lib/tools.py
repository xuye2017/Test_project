import pymysql,redis
from conf_api import setting
import  hashlib
def op_mysql(sql):
	conn = pymysql.connect(host=setting.MYSQL_HOST, user=setting.USER,
                           password=setting.PASSWORD,
                           port=setting.PORT,
                           charset='utf8', db=setting.DB)
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

def op_redis(k,v=None,expired=0,db=0):
	r = redis.Redis(host=setting.REDIS_HOST,password=setting.PASSWORD,port=setting.PORT,db=db)
	if expired>0:#传了失效时间
		r.set(k,v,expired)
		res = 'ok'
	elif v:
		r.set(k,v)
		res='ok'

	else:
		res = r.get(k)
		if res: #这里是判断有没有get到数据
			res = res.decode()
		else:
			res = None
	return res

def md5_passwd(st:str):       #限制入参的类型为string，设置必须传入字符串，不传就会报错
	bytes_st = st.encode()    #将字符串转化成byte类型
	m= hashlib.md5(bytes_st)  #构建MD5对象
	return m.hexdigest()      #返回加密结果
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