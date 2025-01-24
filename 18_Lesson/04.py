def faktoriyal(san):
    if san < 0:
        return "Yalnys sani pozitiv san yazyp gor"
    faktoriyal = 1
    for i in range(1, san + 1):
        faktoriyal *= i
    return faktoriyal

ulanyjy_san = int(input("1 san giriz: "))
print(f"Faktoriyal: {faktoriyal(ulanyjy_san)}")