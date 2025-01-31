print('''
Jemi 10 sorag
''')

import random
jem1 = 0
jem2 = 0
for i in range(1, 11):
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    print(f"{i} - nji sorag\n{a} + {b} =?")
    jogap = int(input("Your answer: "))
    if jogap == a + b:
        print("corect!")
        jem1 += 1

    elif jogap != a + b:
        print(f"Your answer is incorecct! Corecct answer is {a + b}")

print("***Your result***")
print("Quastion: 10")
print(f"Corecct answer: {jem1}")
print(f"Incorecct answer: {jem2}")
print(f"{jem1 * 100 / 10}%")