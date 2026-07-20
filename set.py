# # #set=unordered collection of unique element.
# # #unordered:no index fix
# # #mutable
# # #not allow duolication element:if we write so its not print.
# # set element must be immutable type such as number ,string,or tuple.
# # stntax
# # variable={value,value1}
# # no_value={}#={"
# # print(type(n0_value))
# # empty=set()
# # print(type(empty))  






# set()
# print(type(empty_set)
# =
# empty_set={} 
# print(type(empty_set))

# value=()
# print(type(value)
      
# student={"amit","sona","mahak"}
# print("sona" in student)
# print(1 not in student)

# student.add("jiya")
# print(student)
# set1={1,3,39}
# set2={84,78,94}
# set1.union(set2)
# print(set1)

# student={"amit","jiya","mona"}
# student.remove("jiya")
# print(student)

# student.discard("mahak")
# print(student)
# student.update([2,4,6,8])
# print(student)

# s={20,40,50,56}
# s1={86,94,50,78}
# print(s.union(s1))
# print(s.intersection(s1)) 
# print(s.difference(s1)) # remove commen element and print first set
# print(s.symmetric_difference(s1))#remove comman element 
# print(s)
# x={1,2,3,4,5,6,7,8}
# x.pop() # last element delet 
# print(x)
# print(max(x)) #largest value print
# print(sum(x)) 
# #iempty_setssubset: the first of the set are in the second set.
# print(x.issubset(x1))
# #issuperset:the first set contains all elements all element of the second set.
# print(x.issuperset(x1))
# #disjoint:the two set share no element.or all different element will be store
# print(x.isdisjoint(x1))


a=["janviverma@gmail.com","mahisain@gmail.com","priya@gmail.com","janviverma@gmail.com"]
new_email=set(a)
print(new_email)