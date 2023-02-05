t=()
print(type(t))
t=(1,True,2,3,4,5,[1,3,4,5,])
print(t)

# print(t.count(3))
# print(t.count("abc")
print(t.index(3))
print(t.count(True))
# t[0]=345
# print(t[0])
# tuples are immutable
# and list is mutable
# 'compare lisrt'
# l=[1,2,34,5,5]
# l[0]=15
# print(l[0])
#  itreate tuple
# for i in t:
#     print(i,)
# for i in t:
#     print(i,type(i))

t2=(1,2,3,4,5)
# print(t2*3)

print(max(t2))
print(min(t2))
'''note :- tuples are basically follows immutablity concept where it is not allow to change any element'''
''''where tuples is used
when we want my password is not changed by anyone we use tuples'''

t1=(12,3,4,5)
t3=(t1,t2)
t3=(t1+t2)
print(t3)
del t3
# print(t3) tuples is deleted
print(len(t1))
print(1 in t1)