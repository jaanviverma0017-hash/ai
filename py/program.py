student=(int(input("enter the student name:")))
student_no=[(input("enter the student no.:")),
            int(input("enter the student roll/no.:"))]
 


student_marks=[int(input("enter the student maths marks:")),  
             int(input("enter the student hindi marks:")),
             int(input("enter the student science marks:")),
             int(input("enter the student english marks:")),
             int(input("enter the student social science marks:"))]
print(student_marks .sum())
print(student_marks . average())
print(student_marks .grade)

if student_marks>90:
     print("grade A+")
elif student_marks>80:
     print("grade A")
elif student_marks>70:
     print("grade B")    
elif student_marks>60:
     print("grade C")    
elif student_marks>50:
     print("grade D")   
elif student_marks<40:
     print("fail")         
 
else:
    print("invalid marks,ask again") 
