def educitonal_sys():
    print("Welcome to Educitonal system")

    students = {}
    while True:
        name = input("Enter student's name (done): ").capitalize()

        if name == ("Done"):
            break

        grade = input(f"Enter {name}'s grade: ")

        students[name] = int(grade)

    for i, j in students.items():
        if j >= 90:
            print(f"{i} has an A. Exellent work!")

        elif j >= 75:
            print(f"{i} has an B. Good job!")

        elif j >= 60:
            print(f"{i} has an C. Ozune uns bermeli!")

        else:
            print(f"{i} has failed. kop oka jigimjan!")

    if students:
        average = sum(students.values()) / len(students)
        print(f"Class average: {average:.2f}")

educitonal_sys()