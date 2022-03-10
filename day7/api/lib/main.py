import os
import flask, json
import time
from lib.tools import op_redis,op_mysql,md5_passwd
# 接口，后台服务
server = flask.Flask(__name__)  # 把咱们这个app这个python文件当做一个server

@server.route('/get_user', methods=['get', 'post'])
def get_all_user():
	sql = 'select * from bt_stu;'
	res = op_mysql(sql=sql)
	response = json.dumps(res, ensure_ascii=False)  # 把list转成json
	return response  # return 的时候只能return字符串


@server.route('/add_user', methods=['post'])
def add_user():
	user_id = flask.request.values.get('id')  # 这里的参数就是调用接口的时候传入的参数
	username = flask.request.values.get('u')  #
	if user_id and username:
		sql = "insert into stu values ('%s','%s');" % (user_id, username)
		res = op_mysql(sql=sql)
		response = {'code': 308, 'msg': '添加成功'}
	else:
		response = {'code': 503, 'msg': '必填参数未填！'}
	return json.dumps(response, ensure_ascii=False)


@server.route('/ddddd')
def login():
	username = flask.request.values.get('u')
	password = flask.request.values.get('p')
	# username = " ' or '1'='1 "
	username = "'; show tables; --"
	sql = "select * from user where username='%s' and password='%s';" % (username, password)
	print('sql...', sql)

	# select * from user where username='' or '1'='1' and password='';
	# select
	# select * from user where username='nhy' and password='123456';
	print(sql)
	# res = op_mysql(sql)
	res = '1'
	print(res)
	if res:
		response = {'msg': '登录成功'}
	else:
		response = {'msg': '账号/密码错误'}
	return json.dumps(response)


# server.run(port=8080,debug=True)
@server.route('/login', methods=['get'])
def login1():
	username = flask.request.values.get('username', '')
	password = flask.request.values.get('password', '')
	sql = "select * from user where username='%s' and password='%s';" % (username, password)
	res = op_mysql(sql)
	if res:
		k = "session:%s" % username
		v = str(time.time()) + username  # 当前时间戳+用户名然后md5一次，作为session
		session = md5_passwd(v)
		op_redis(k, session, expired=6000, db=2)
		msg = {'code': 309, 'msg': '登录成功', 'session': session}
		response = flask.make_response()  # 如果加cookie的话，就用make_response()
		response.set_data(json.dumps(msg,ensure_ascii=False)) #添加返回的数据
		response.set_cookie('session',session)              #添加cookie
		response.set_cookie('zheshiwosetdecookie','hahaha')
	else:
		response = json.dumps({'code': 308, 'msg': '账号/密码错误'},ensure_ascii=False)
	return response


@server.route('/cmd')
def cmd():
	comand = flask.request.values.get('cmd')
	if comand:
		res = os.popen(comand).read()
		return res

	# 1、先验证用户是否登录   username，session
	# 2 验证session是否正确，判断用户传过来的session和redis里面存的是否一致
	# 3、如果一致的话，返回双色球信息
	# 4 、 如果不一致的话
	# 1、sesison不一样的话，提示非法
	# 2、sesiion不存在的话，提示用户未登录


@server.route('/get_seq')
def get_seq():
	username = flask.request.values.get('username')
	session = flask.request.values.get('session')  # 用户传过来的 session
	k = 'session:%s' % username
	print('k...', k)
	# session:lzc
	# session:lzc
	redis_session = op_redis(k, db=2)
	if redis_session:  # 判断是否从redis里获取到数据
		if session == redis_session:  # 如果用户传的session和redis保存的一致
			response = op_mysql('select red,blue from seq;')
		else:
			response = {'code': 101, 'msg': 'session非法！'}
	else:
		response = {'code': 100, 'msg': '用户未登录！'}
	return json.dumps(response, ensure_ascii=False)


@server.route('/get_seq2')  # 这种是从cookie里获取到的。
def get_seq2():
	username = flask.request.values.get('username')
	session = flask.request.cookies.get('session')  # 这个是从cookie里面获取到的 用户传过来的 session
	k = 'session:%s' % username
	print('k...', k)

	redis_session = op_redis(k, db=2)
	if redis_session:  # 判断是否从redis里获取到数据
		if session == redis_session:  # 如果用户传的session和redis保存的一致
			response = op_mysql('select red,blue from seq;')
		else:
			response = {'code': 101, 'msg': 'session非法！'}
	else:
		response = {'code': 100, 'msg': '用户未登录！'}
	return json.dumps(response, ensure_ascii=False)
