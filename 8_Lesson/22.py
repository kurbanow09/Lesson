sana = 0
a = int(input("Enter A: "))
b = int(input("Enter B: "))
for n in range(b, a - 1, -1):
    sana += 1
    print(f"{n}")
print("The amount", sana)