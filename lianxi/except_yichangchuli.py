

# sum =0
#
# for i in range(0,101):
#     sum += i
#
# print(sum)

def func():
    str1 = input('输入数字:')
    try:
        num = int(str1)
        assert (num >= 10), 'num不能少于10'
        print(num)
    except (ValueError,AssertionError) as e:
        print(e)
        print('不是数字')
    else:
        print('没有发生异常')

    finally:
        print('都会执行')


if __name__ == "__main__":
    func()