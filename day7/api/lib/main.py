import flask,json
from lib.tools import op_mysql  #op_mysql()
# flask 轻量级的，web开发框架，开发后台服务。接口，后台服务
server = flask.Flask(__name__) #把咱们这个app这个python文件当做一个server
@server.route('/get_user',methods=['get','post'])
def get_all_user():
	sql = 'select * from bt_stu;'
	res = op_mysql(sql=sql)
	response = json.dumps(res,ensure_ascii=False) #把list转成json
	return response #return 的时候只能return字符串

@server.route('/add_user',methods=['post'])
def add_user():
	user_id = flask.request.values.get('id')  #这里的参数就是调用接口的时候传入的参数
	username = flask.request.values.get('u') #
	if user_id and username:
		sql = "insert into stu values ('%s','%s');"%(user_id,username)
		res = op_mysql(sql=sql)
		response = {'code':308,'msg':'添加成功'}
	else:
		response = {'code':503,'msg':'必填参数未填！'}
	return json.dumps(response,ensure_ascii=False)


# server.run(port=8080,debug=True)



