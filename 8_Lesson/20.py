n = 1
num = int(input("Enter a number: "))
for num in range(1, num + 1):
    if n % 2 == 0: 
        print(n, n * "&")
    else:
        print(n, n * "@")
    n += 1