student = []
n = int(input("Enter the number of student: "))

for i in range(n):
    print(f"\nEnter details of student {i + 1}")

    name = input("Enter Name: ")
    roll_no = input("Enter Roll No:")

    marks = []

    # Taking 5 subject marks 
    for j in range(5):
        while True:
            mark = int(input(f"Enter marks of student {j + 1} (0-100):"))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invaild marks! Please enter marks between 0 and 100.")
    total = sum(marks)
    average = total / 5

    # Finding Grade
    if average >= 90:
        grade ="A+" 
    elif average >=80:  
        grade ="A"
    elif average >=70:
        grade ="B"
    elif average >=60:
        grade ="C"
    elif average >=40:
        grade ="D"    
    else:
        grade = "Fail"    

    # Store data in a list 
    student = [name, roll_no,marks, total, average, grade]
    student.append(student)     
    #Display Result
    print("\n========== STUDENT REPORT ==========")

    for student in student:
        print("\n---------------------------------------")
        print("Name       :", student[0])
        print("Roll_no    :", student[1])
        print("Marks      :", student[2])
        print("Total      :", student[3])
        print("Average    :", round(student[4], 2))
        print("Grade      ")