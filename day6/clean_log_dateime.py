import os,datetime
def clean_log(path):
	if os.path.exists(path) and os.path.isdir(path):
		today = datetime.date.today()  #2017-01-02
		yesterday = datetime.date.today()+ datetime.timedelta(-1)
		before_yesterday = datetime.date.today()+ datetime.timedelta(-2)
		file_name_list = [today,yesterday,before_yesterday]
		for file in os.listdir(path):
			file_name_sp = file.split('.')
			if len(file_name_sp)>2:
				file_date = file_name_sp[1] #取文件名里面的日期
				if file_date not in file_name_list:
					abs_path = os.path.join(path,file)
					print('删除的文件是%s,'%abs_path)
					os.remove(abs_path)
				else:
					print('没有删除的文件是%s'%file)
	else:
		print('路径不存在/不是目录')
clean_log(r'')