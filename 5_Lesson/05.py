print("""
<<<Menu>>>
1. Tea
2. Coffee
3. Water
4.Fruit juice""")
drink = int(input("What would you like to drink? "))
if drink == 1:
    print("You choose Tea")
elif drink == 2:
    print("You choose Coffee")
elif drink == 3:
    print("You choose Water")
elif drink == 4:
    print("You choose Fruit juice")
else:
    print("I did't understand")