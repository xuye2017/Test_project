#   1、如果同一个ip地址60s以内访问超过200次，那么就把ip加入黑名单
#需求分析：
#1、60s读一遍文件
#2、分割，取到第一个元素，IP地址
#3、把所有的ip加入一个list里，如果ip次数超过200次，加入黑名单

import  time

point = 0 #文件指针

while True:
    ips =[]#存放所有的ip地址
    blk_set = set()
    with open('assess.log',encoding='utf-8') as  f:
        f.seek(point)   #seek() 方法用于移动文件读取指针到指定位置
        for line in f:
            ip = line.split()[0]
            ips.append(ip)
            if ips.count(ip)>199:
                blk_set.add(ip)
        for ip in blk_set
                print('加入黑名单')
        point = f.tell()   #tell() 方法返回文件的当前位置，即文件指针当前位置
        time.sleep(60)