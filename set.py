s={}
print(type(s))
# in this case it telling it is dict

s1={1}
# in this case it telling it is set
print(type(s1))
s2={1,1,1,2,43,54,65,6,43,23,2,1}
print(s2)
# # set always store only unique element
# #  also set is unordered
# print(list(s2))
# print(set(list(s2)))
# # s4={1,2,3,4,[1,2,4,3]}
# # print(s4)
# # list is changed
s5={1,2,3,4,(3,6,67)}
# print(s5)
# s6={'ttt','TT'}
# # print(s5[0])
# for i in s5:
#     print(i)
s5.add(111)
print(s5)
print(len(s5))
print(s5.pop())
print(s5.clear())
