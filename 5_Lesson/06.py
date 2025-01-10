weather = int(input("Enter a number of temperature: "))
if weather <= 0:
    print("Freezing weather")
elif weather <= 10:
    print("Very cold weather")
elif weather <= 20:
    print("Cold weather")
elif weather <= 30:
    print("Normal")
elif weather <= 40:
    print("Hot")
else:
    print("Very hot")