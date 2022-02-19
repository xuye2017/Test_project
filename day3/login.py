# username =[] #所有的用户名
# for i in range(3):
#     username=input('用户名：').strip() #strip不能为空
#     passwd=input('密码：').strip()
#     if usernames.count(username)==0:   #判断找到的个数是否为0，为0的话代表这个用户没有被注册过
#         print('注册成功')
#         usernames.append(username)
#     else:
#         print('该用户已经被注册')


all_user={ }
while True:
    username = input('用户名：').strip()  # strip不能为空
    passwd = input('密码：').strip()
    cpasswd = input('再次输入密码：').strip()
    if username and passwd and cpasswd:
        if username in all_user:
            print('用户已存在，请重新输入')
        else:
            if passwd ==cpasswd:
                all_user[username] =passwd
                print('欢迎登录')
                break
            else:
                print('两个密码不一致')
    else:
        print('用户名和密码不能为空')


