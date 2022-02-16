#assert 是断言，python中的assert方法会首先判断括号中的是否为真

a = 1
b = 0
try:
    assert (a > 1)
    c = a / b
except (ZeroDivisionError, AssertionError) as e:
    print('发生异常', e)

else:
    print('没有发生异常')

finally:
    print('不管有没有异常，都会执行')