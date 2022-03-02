#函数 方法 功能  函数把一推代码组合在一起，变成一个整体;函数不调用不会被执行；提供代码的复用性
#返回值：1、如果想获取到函数的结果，那么必须return；2、如果函数没有写return的话，返回值是None，返回return不是必须写的。

def hello(file_name,content=''):
    f = open(file_name,'a+',encoding='utf-8')
    if content:
        f.write(content)
    else:
        f.seek(0)
        res = f.read()
    f.close()


hello('xuye.txt','hhh') #调用

a = 1 #全局变量

def test():
    global a #申明全局变量
    print('里面的',a)
test()
print('外面的',a)