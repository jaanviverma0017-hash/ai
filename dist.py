







student={
  "name":"janvi",
  "age":20,
  "village":"bhojawas"
}
print(student)
print(len(student))
name=dict()
print(name)
print(type(name))

pairs=[("a",1),("b",2),("c",3)]
d=dict(pairs)
print(d)

mix=[("age",20),("name","jiya"),("number",4),("value",True,)]
d=dict(mix)
print(d)

member1=dict(name="janvi",
             value=12,
             collage="rps")
print(member1)            

#using get (): you can also use get method to access dictionary item.
#print(student.get("name"))
#print(student.get("email"))
#print(student.get("email","email not available"))
# adding and update dict items
# adding a new key- value pair
# student["city"]="delhi"
# print(student)
#// updateing an existing value 
#student["age"]
#print(student)

student={
    "name":"jaanvi",
    "age":20,
    "course":"bca"
}
student["age"]
print(student)
print(student)
print(student.pop("age"))
print(student)
print(student)
#pop item
student.pop()
print(student)
##// A dict can contain another dictionary 
# print(student["student_1"[name]])
#print(student["student_2"]["course"])


