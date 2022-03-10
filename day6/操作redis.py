import redis


r = redis.Redis(host='127.0.0.1',port=6379,password='foobared',db=2)#连上redis
print(r.get('hahahsfdfsdf'))
#r.set('nhy_session','201801211505') #set数据
# print(r.get('马佩佩').decode()) #redis里面取出来的数据都是bytes类型的，所以要用.decode方法转成字符串
# r.delete('马佩佩')#删除一个
#r.setex('nhy','hahah',20) #可以指定key的失效时间，单位是秒‘

# set  get delete setex 都是针对string类型的  k - v

#hash类型
# r.hset('sessions','nhy','123456')  #插入数据
# r.hset('sessions','ybq','1234562')
# r.hset('sessions','xsr','1234561')
#print(r.hget('sessions','xsr'))  #获取数据
# redis_data = r.hgetall('sessions') #获取到hash类型里面所有的数据
# all_data = {}
# for k,v in redis_data.items():  #把hash类型里面所有的数据转成正常的字典
# 	k = k.decode()
# 	v = v.decode()
# 	all_data[k]=v
#hash类型没有过期时间

#下面这种是有层级的
# r.set('txz:ybq','没交')   #
# r.set('txz:haixia','交了') #
# print(r.keys())#获取所有的key
# print(r.keys('txz*')) #以txz开头的key
# print(r.type('sessions'))#获取key的类型

# 把redis里面一个数据库的东西，弄到另外一个数据库里。
# 1、建立两个redis连接
	#1、src
	# 2、 target
#2、获取到所有的key，kyes ()
# 3、判断key的类型，string hash
