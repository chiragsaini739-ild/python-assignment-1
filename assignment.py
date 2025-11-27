# Name:[Chirag Saini]
# Roll No:[250166004]
# Course:BCA[Cyber Security]
# Semester:1st
# Subject:Problem Solving with Python
# Assignment:Unit-1 Mini Project
# Title:Student Profile Console App
print("========================================")
print("   Welcome to Student Profile System")
print("========================================")
print("This is a tool collects your details of students")
print("Thus creating a Pre-Formatted ID/Profile Card")
student_full_name=str(input("Enter Your Full-Name: "))
roll_number=int(input("Enter Your Roll Number: "))
program=str(input("Enter Your Program (i.e- BCA): "))
university_name=str(input("Enter Your University Name: "))
city=str(input("Enter Your City: "))
age=int(input("Enter Your Age: "))
hobby=str(input("Enter Your Hobby: "))

print("---------------------------------------")
print("        STUDENT PROFILE SYSTEM          ")
print("---------------------------------------")
print(f"Name: {student_full_name}")
print(f"Roll No: {roll_number}")
print(f"Course: {program}")
print(f"University: {university_name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print("----------------------------------------")
print("Welcome to Python Programming!!")

saving_choice=input("Do you want to save your profile?(yes/no): ").lower()
if saving_choice=="yes":
    with open("student_profile.txt","w") as file:
        file.write("------------------------------------\n")
        file.write("      STUDENT PROFILE SYSTEM        \n")
        file.write("------------------------------------\n")
        file.write(f"Name: {student_full_name}\n")
        file.write(f"Roll No: {roll_number}\n")
        file.write(f"Course: {program}\n")
        file.write(f"University: {university_name}\n")
        file.write(f"City: {city}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hobby: {hobby}\n")
        file.write("----------------------------------------\n")
        file.write("Welcome to Python Programming!\n")
    print("Profile saved as'student_profile.txt'")
else:
    print("Profile saved failed")