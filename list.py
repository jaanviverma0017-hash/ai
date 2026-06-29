# marks=[1,2,3,6,2,3,4,5,1]
# print(marks)
# print(type(marks))
# #a=[1,2,3,4,5]
# print(a[1:3])         
# print(a)
# a=[1,2,3,4,5]
# print(a[-4:-1])


t= (1,2,3,4,5,6,7,8,9,10)
# print(type(t))

a=list(t)






abc=("jiya","teena",(1,2,3),(4,5,6),"mahak")
print(abc)
abcd=list(abc)
abcd.pop(3)
abcd.pop()
print(abcd)
#abcd.remove("mahak")
#print(abcd)

abc=tuple(abcd)
print(abc)


a=2*abc
print(a)


b=(9,8,7)
c=(6,5,4)
d=b+c
print(d)

number=((1,2,3),(3,4,5),(5,6))
n1,n2,n3=number 
print(n1,n2)

name=(("mahak"),("jiya"),("teena"),(1,0,0),2,4,5)
n1,n2,n3,n4,*n5=name
print(n1,n2,n4,n3,n5)
