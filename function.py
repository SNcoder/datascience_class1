# # # def test():
# # #     pass
# # def test():
# #     a=1*2+4
# #     # print("this is a function")
# #     return a
# # # print(test()+'era')
# # print(type(test()))
# # # def tes2():
# # #     return 1,2,34,'rr'
# # # # print(tes1()[1])
# # # # a,c,v=1,2,6
# # # # print(a,c,v)
# # # a,b,c,d=tes2()
# # # print(a)
# # # def test3(a,b):
# # #     c=a+b
# # #     return c
# # # print(test3(b=98,a=2))
    
# # # def test4(l):
# # #     l1=[]
# # #     for i in l:
# # #         if type(i)==int or type(i)==float:
# # #                  l1.append(i)
# # # #     return l1
# # # def test4(l):
# # #     l1=[]
# # #     for i in l:
# # #         if type(i)==int or type(i)==float:
# # #             l1.append(i)
# # #         else:
# # #             for i  in l:
# # #                 if type(i)==list:
# # #                     l1.append(i)
# # #             return l1

# # # r=[1,4,56,8,9,'jk','jdj',True,[2,3,4,5,560]]    
# # # print(test4(r))
# # # def t1(a,b,c,d,w):
# # #     pass
# # # print(t1(1,2,3,4,5))

# # # def t(*a,c):
# # #     return a,c
# # # print(t(1,2,3,4,5,6,c='aaa'))

# # def t4(*args):
# #     l=[]
# #     for i in args:
# #         if type(i)==list:
# #             l.append(i)
# #     return l
# # print(t4(1,2,3,4,[3,4,5,6],"w",True))

# # def t5(**ke):
# #     return ke
# # print(t5( a='k' , abc="lkh",c=1,w2='a'))
# # # print(t5()['a'])
# # def t6(**k6):
# #     for i in k6.keys():
# #         if type(k6[i])==list:
# #             return i,k6[i]
# # print(t6(a=4,c=6,r=8,d=[54,6,7,78],f=True))

# def t8(*a,**k):
#     return a,k
# print(t8(1,2,3,4,s=34,t=9,c=8))

d={2:4,24:7}
print(d)