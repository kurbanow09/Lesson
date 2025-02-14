file_path = "Book.txt" 

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read().upper()  

with open(file_path, "w", encoding="utf-8") as file:
    file.write(content)

print("Bash harplara uytgedildi")