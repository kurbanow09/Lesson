import random

number_count = 0
picture_count = 0

print("Output:\n")
for i in range(1, 11):
    result = random.choice(["picture", "number"])
    print(f"{i} {result}")
    
    if result == "picture":
        picture_count += 1
    else:
        number_count += 1

print(f"\nNUMBER: {number_count}")
print(f"PICTURE: {picture_count}")

most_tossed = "PICTURE" if picture_count > number_count else "NUMBER"
print(f"\nMost tossed: {most_tossed}")