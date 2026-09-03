#Alejandra Ibarr
#Lab 6

#Created a function for modifying student list.

def user_response(response, students):
    if response == 1:
        new_name = input ("Please enter name of new student. ")
        students.append(new_name)
        for i in range(len(students)):
            print(students[i])
    elif response == 2:
        for i in range(len(students)):
            print(i+1,".)", students[i])
        id = int(input("Please enter which index 1-5 to change. "))
        id = id - 1 
        mod_name = input("Please enter modified name. ")
        students[id] = mod_name
        for i in range(len(students)):
            print(students[i])
    else:
        for i in range(len(students)):
            print(i+1, ".) ", students[i])
        id = int(input("Please enter index 1-5 you wish to delete. "))
        id = id - 1
        students.pop(id)
        
        for i in range(len(students)):
            print(students[i])

    return students 

student_list = ["Ismael", "Viviana", "Adriel", "Nubia", "Azrael"]

for student in student_list:
    print(student)

menu_display = ["Menu:", "1.) Add a student", "2.) Modify a student name", "3.) Remove student"]

for item in menu_display:
    print(item)

num = int(input("Please enter 1, 2, or 3 for which option you want to do. "))
user_response(num, student_list)

