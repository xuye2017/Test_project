a = 1
b = 0
try:
    c =1 / 0
except BaseException as e:
    print('发生异常',e)

else:
    print('没有发生异常')

finally:
    print('不管有没有异常，都会执行')

