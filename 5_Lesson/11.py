a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
elif d == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    print("No real roots")