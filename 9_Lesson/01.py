for i in range(1, 6):
    san = int(input(f"{i} - enter a number: "))
    if i == 1:
        iu = san
        ik = san
    elif iu < san:
        iu = san
    elif ik > san:
        ik = san
print("Max number is:", iu)
print("Min number is:", ik)

