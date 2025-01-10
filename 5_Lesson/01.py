grade = int(input("Enter your grade: "))
if grade > 100 or grade < 0:
    print("Invalid")
elif grade >= 85:
    print("5")
elif grade >= 70:
    print("4")
elif grade >= 50:
    print("3")
elif grade <= 49:
    print("2")