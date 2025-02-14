file_path = "Book.txt" 

letter_count = 0
zero_count = 0

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    letter_count = sum(1 for char in content if char.isalpha())  
    zero_count = content.count('0')  

print("Harplaryň mukdary:", letter_count)
print("Sifirleriň mukdary:", zero_count)