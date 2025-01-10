t = int(input("Uc belgili san girizin:\n "))
a = t % 10
b = t // 100
c = t // 10 % 10
print(f"{a}{c}{b}")