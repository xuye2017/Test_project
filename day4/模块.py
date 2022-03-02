#一个python文件就是一个模块 1、标准模块 ，python自带的，不需要安装 2、第三模块，pip install  3、自己写的

nums =[0,1,3,5,6,7,9]
# new_nums =[]
# for n in nums:
#     n =str(n)
#     new_nums.append(n)
# print(new_nums)
#     #列表推导式
new_nums =[str(n) for n in nums]
print(new_nums)