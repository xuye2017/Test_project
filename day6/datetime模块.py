import datetime,time

print(datetime.datetime.today())#当前时间，也可以用now一样的
print(datetime.datetime.today().strftime('%Y%M%D'))
print(datetime.datetime.today()+datetime.timedelta(-3))#三天前,如取3天后就写3

print(datetime.date.today())#取当天的日期，只是日期
dt = datetime.datetime(2022,3,4,15) #用指定日期时间创建datetime
print(type(dt))
print(dt.timestamp())#把datetime转换为timestamp