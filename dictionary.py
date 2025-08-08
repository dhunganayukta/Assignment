
D={}
n=int(input("how many students?"))
for i in range(n):
    stu_name=input("enter student name:-")
    stu_age=int(input("enter student age"))
    stu_university=input("enter student university")
    D[stu_name]=stu_age and stu_university
print("created dictionary:-")
print(D)
var=input("enter the student name to display its age and university")
print(D[var])
