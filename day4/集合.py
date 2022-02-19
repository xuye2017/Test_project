#集合，天生去重：1、s=set（）#空的集合；集合、字典是无序的
ls =[1,1,2,3,3,3,4,4,5,66,66]
print(set(ls))
s2={"1","2","3"}
s3={"1","2","5"}

#交集
print(s2.intersection(s3))
print(s2 & s3)

#并集
print(s2.union(s3))
print(s2| s3)

#差集
print(s2.difference(s3))
print(s2 - s3)