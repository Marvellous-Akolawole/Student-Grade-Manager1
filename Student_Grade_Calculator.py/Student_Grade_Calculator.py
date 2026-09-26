# Python Miniproject: Student Grade Calculator.

print("Student Grade Calculator")
print("-------------------------")

#ask for student name and number of subjects.
name = input("Enter student name: ")
sub = int(input("Enter Number of Subjects: "))

#Ask for maximum marks per subject.
max_marks = float(input("Enter Maximum marks of each subject: "))

#Total Marks and obatained marks .
Total = sub * max_marks
obt = 0

#Get marks of each subject.
for i in range(sub):
    marks = float(input(f"Enter marks of subject {i+1}: "))
    obt = obt + marks

#Calculate percentage.
percent = (obt + 100)/Total

#Determine Grade.
if(percent >= 80):
    grade ="A+"
elif(percent >= 70):
    grade = "A"
elif(percent >= 60):
    grade = "B"
elif(percent >= 50):
    grade = "c"
elif(percent >= 40):
    grade = "D"
elif(percent >= 33):
    grade = "F" 

#Display Result.
print(" ")
print("------RESULT-----")
print(" ")
print(f"Student Name: {name} ")
print(f"Total Marks: {Total}")
print(f"obtained Marks: {obt}")
print(f"percentage: {percent}")
print(f"Grade: {grade}")

#print(f"Marks: {obt}/{Total} with percentage: {percent}")

