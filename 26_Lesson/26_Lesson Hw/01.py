choice = input("Add Student (1) | Show Students (2) | Remove Student (3) | Exit (4): ")

if choice == "1":
    name = input("Student Name: ")
    course = input("Course: ")
    price = input("Price: ")
    add_student(name, course, price)

elif choice == "2":
    show_students()

elif choice == "3":
    name = input("Name of the student to remove: ")
    remove_student(name)

elif choice == "4":
    print("Thank you for using our program!")
    break