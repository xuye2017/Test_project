import  time
# time.sleep(2) #等待几秒
# print(int(time.time())) #当前时间戳
# cus_time = time.strftime('%Y-%m-%d %H:%M:%S')
# print(cus_time)
# print(time.gmtime())#默认取标准时区的时间元组，如果传入了一个时间戳，那么就把这个时间戳转换成时间元组
# print(time.timezone)#和标准时间相差了几个小数
cus_time = time.localtime(1516005840)
res = time.strftime('%Y-%m-%d %H:%M:%S',cus_time)

def timestampeToStr(time_strmp,format='%Y%m%d%H%M%S'):
    cus_time = time.localtime(time_strmp) #时间戳转换成时间元组
    res =time.strftime(format,cus_time)  #再把时间元组转成格式化好的时间
    return  res
# t = timestampeToStr(1516005840,'%Y-%m-%d')
# print(t)

def strToTimestamp(time_st,format='%Y%m%d%H%M%S'):
    t =time.strftime(time_st,format) #把格式化好的时间转成时间元组
    res =time.mktime(t) #时间元组转成时间戳
    return  res