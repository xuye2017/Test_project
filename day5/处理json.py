import json
d ={
    'car':{'color':'red','price':'100','count':50},
    '春风吹':{'color':'red','price':'100','count':50},
}


res = json.dumps(d,indent=4,ensure_ascii=False) #把字典转成json,indent多少缩进;ensure_asciiw为了不让中文乱码
print(res)

f = open('f1','w',encoding='utf-8')
f.write(res)