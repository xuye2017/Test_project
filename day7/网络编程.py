import json
import urllib.request
import requests
#发送get请求组
url ='http://xxx？yyy=zzz'
#以下不好用
# urllib.request.urlopen(url) #发送请求
# jieguo = res.read().decode()  #获取结果
#
# json.loads(jieguo)  #转换json类型

req=requests.get(url)
json.loads(req.text) #h获取结果直接就是字典

#发送post请求
url ='http://xxx？yyy=zzz'
data ={'xxx':'xxxx','cccc':'ccdd'}
req = requests.post(url,json=data) #发送post请求，第一个参数是url，第二个参数是请求的数据
print(req.json())

#入参json类型
url ='http://xxx？yyy=zzz'
data ={'xxx':'xxxx','cccc':'ccdd'}
req = requests.post(url,data)

#添加cookie

url ='http://xxx？yyy=zzz'
data ={'xxx':'xxxx','cccc':'ccdd'}
cookie={'sign'：'82168hjhjhj231203jkklll'}
req = requests.post(url,data,cookies=cookie)

#添加header
url ='http://xxx？yyy=zzz'
header={'referre':'http://hhh.xx.cn/'}
req = requests.post(url,headers=header)
print(req.text)


#上传文件
url ='http://xxx？yyy=zzz'
f = open(r'路径')
r = requests.post(url,files={'file':f})

#下载文件
url ='http://xxx？yyy=zzz'
r = requests.get(url)
r.status_code  #获取请求的状态码
r.content  #获取返回结果二进制
fw =open('C:/bt.jpg','wb')
fw.write(r.content)
fw.close()