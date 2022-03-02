import sys,os
def clean_log(path):
    print('日志已经清理')

def back_db(db_name):
    print('数据库已备份')


args =sys.argv
if len(args)>1:
    path = arge[1]

    if os.path.isdir(path): #判断是不是目录
        clean_log(path)
    else:
        print('必须上传')

else:
    print('运行这个Python文件需要传入一个路径！\n'
          'eg: python clear_log.py /usr/tomcat/logs')