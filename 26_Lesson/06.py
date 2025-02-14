with open ("Numbers.txt", "r") as fayl:
    A = fayl.read().split()
    print(A)

    B = []
    for i in A:
        B.append(int(i))

    C = []
    D = []
    for i in B:
        if i > 0:
            C.append(i)
        else:
            D.append(i)


with open ("polizitel.txt", "w") as fayl:
    for  i in C:
        fayl.write(str(i)+"\t")

with open ("otrisatel.txt", "w") as fayl:
    for i in D:
        fayl.write(str(i)+"\t")