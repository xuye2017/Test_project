import hashlib
#md5,以下是两种方式

# xuye_pwd='bugggkkk' #
# m = hashlib.md5()#
#
# m.update(xuye_pwd.encode())#加密，不能字符串，只能传bytes类型，二进制
#
# print(m.hexdigest()) #加密后的结果

def md5_password(st:str):#限定了入参的类型，只能为string类型
    bytes_st =st.encode() #转成二进制类型
    m = hashlib.md5(bytes_st) #加密
    return m.hexdigest()  #返回加密后的结果
res = md5_password('233333333')

print(res)