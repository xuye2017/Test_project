class MyExcpet(Exception):
     def __init__(self, errorInfo,code=100):
         super().__init__(self)
         self.errorinfo = errorInfo
         self.code = code

     def __str__(self):
        return  self.errorinfo
try:
    raise MyExcpet('注册异常',200)  #使用raise抛出异常 触发异常后，后面的代码就不会再执行
except MyExcpet as e:
    print(e.code)
    print(e)

if __name__ == "__main__":
    pass