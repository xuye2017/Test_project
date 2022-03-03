import random,string

res = random.uniform(1,9)#取随机小数
print(res)
print(round(res,2)) #保留几个小数
print(random.random()) #取0-1之间随机小数

s=['a','b','c','d','f']

random.shuffle(s) #洗牌，打乱顺序
print(s)