a = int(input("Uc belgi san girizin:\n "))
print(f"{a}-sanyn sifrlerinin jemi: {(a // 100) + ((a // 10) % 10) + (a % 10)}")
print(f"{a}-sanyn sifrlerinin kop.has jemi: {(a // 100) * ((a // 10) % 10) * (a % 10)}")
