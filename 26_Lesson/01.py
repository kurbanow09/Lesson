name = input("Enter your name: ")
age = input("Enter your age: ")

with open("users.txt", "a") as file:
    file.write(f"Name: {name}, Age: {age}\n")

print("Data saved!")