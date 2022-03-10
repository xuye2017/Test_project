import redis

src_redis = redis.Redis(host='127.0.0.1',port=6379,password='foobared',db=2)#连上redis
target_redis = redis.Redis(host='127.0.0.1',port=6379,password='foobared',db=14)#连上redis
for key in src_redis.keys():
	if src_redis.type(key) == b'string':  #判断key的类型，因为redis数据取出来都是二进制的，所以这里也用bytes
		v = src_redis.get(key) #先获取到原来的数据
		target_redis.set(key,v) #再set到新的里面
	else:
		all_hash_data = src_redis.hgetall(key)   #先获取到hash类型里面所有的数据
		for k,v in all_hash_data.items(): #因为hash类型的获取到之后是一个字典，所以这里循环字典
			target_redis.hset(key,k,v)  #key是外面的大key，k是里面的小k，v就是小k对应的value

