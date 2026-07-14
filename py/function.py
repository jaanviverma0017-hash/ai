# def print_hello():
#     print("hello")

# output = print_hello()
# print(output)   

# def calculate_avg(a, b, c):
#     sum= a + b + c
#     avg = sum/3
#     print(avg)
#     return avg

# calculate_avg(1, 2, 3)

# def cal_prod(a, b):
#     print(a * b , a + b)
#     return a * b , a + b

# cal_prod(4 , 5)
a=5
# b=5
# # def fun(a=4,b):
#     # print(a * b , a + b)
#     return a,b 
# # fun(b=6)   
# # 
# def value(a,b=6):
#     print(a+b , a*b)
#     return a,b
# value(4)

# def message():
#   return print("python")
# value = message()
# print(value)

# def calculate(a,b=2):
#     a = a + b
#     b = a * b
#     return a, b
# x ,y = calculate(3)
# print(x+y)


# def operation(a, b):
#     return a + b
 
# def calculate(x):
#     return operation(x, x * 2)

# print(calculate(4))

# sometime we do not know how many argument will be passed to a function.
# in such cases , we use *args
# *args stores multiple positional argument  as a tuple


#position single star mention

def add_numbers(*numbers):
    total=0
    for num in numbers:
     total += num
    return total
print(add_numbers(10, 20))
print(add_numbers(5, 10, 15, 20))

def show_names(*names):
   for name in names:
    print(name)
show_names("jiya","teena","mahak")      
      
def show_name(greet,*name):
  for name in names:
   print(greet,hello)
show_names("jiya","teena","mahak")

#keywords double star mention 

def show_details(**details):
  for key, value in details.items():
   print(key,":", value)
show_details(names="rohit", age=20, city="delhi")

def create_profile(**user):
  print("user profile")
  print("name", user.get("name"))
  print("age",user.get("age"))
  print("email",user.get("email"))
create_profile(name="janvi",age=20,email="janviverma@gmail.com")

count=0

def increase():
  global count
  count +=1
increase()
increase()
print(count)






