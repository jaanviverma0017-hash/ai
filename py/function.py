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

# 4. function documentation: docstrings

def square(number):
  return number*number
print(square(5))
print(square.__doc__) 

# type mints in function 
# type hints show what type of data  a function expects and return

def add(a: int, b: int)->int:
  return a + b
print(add(10 , 20))

# lambda function 
# A lambda function is a small anonymous function.
# It is usualiy used for short operation.

# syntax
# lambda argument: expression

square = lambda x: x*x
print(square(6))

add = lambda a, b: a + b
print(add(5, 5))

#map(), filter(),shorted()



# def find_largest(numbers):
#   largest = number[0]
#   for number in numbers:
#     if number > largest:
#      largest = number
#      marks = [45, 78, 92, 61, 89]
#   return largest 
# print(find_largest(marks))



# function calling other function 


def get_square(number):
  return number * number
def print_square(number):
  result = get_square(number)
  print("square:", result)
print_square(9)

# nested function
 
#def outer_function():

# Recursion

# A base condition to stop recursion 
# A function calling itself with a modified argument.

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))  
  


  
  
  






