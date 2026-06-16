print("===== STUDENT RECORD MANAGEMENT SYSTEM =====")

students = []

def add_student():

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print("Roll Number Already Exists!")
            return

    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)
    with open("student.txt", "a") as file:
        file.write(f"{roll},{name},{branch},{marks}\n")

    print("Student Added Successfully!")
def view_students():
    if len(students) == 0:
        print("No Student Records Found")
        return

    print("\n------------------------------------------------")
    print("Roll\tName\t\tBranch\tMarks")
    print("------------------------------------------------")

    for student in students:
        print(
            f"{student['roll']}\t{student['name']}\t\t{student['branch']}\t{student['marks']}"
        )
def search_student():

    roll = input("Enter Roll Number to Search: ")

    for student in students:

        if student["roll"] == roll:
            print("\nStudent Found")
            print("Roll Number :", student["roll"])
            print("Name        :", student["name"])
            print("Branch      :", student["branch"])
            print("Marks       :", student["marks"])
            return

    print("Student Not Found")
def update_student():

    roll = input("Enter Roll Number to Update: ")

    for student in students:

        if student["roll"] == roll:

            print("\nStudent Found")

            student["name"] = input("Enter New Name: ")
            student["branch"] = input("Enter New Branch: ")
            student["marks"] = input("Enter New Marks: ")

            print("Student Updated Successfully!")
            return

    print("Student Not Found")
def delete_student():

    roll = input("Enter Roll Number to Delete: ")

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            print("Student Deleted Successfully!")
            return

    print("Student Not Found")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
