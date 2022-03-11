import sys,os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #取到工程目录
sys.path.insert(0,BASE_PATH)#加入环境变量

from lib.main import server

server.run(port=8989,host='127.0.0.1',debug=True)

#host 0.0.0.0 代表一个局域网里面所有人都可以访问。
