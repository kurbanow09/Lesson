A={"Kitap":"book",
   "Nilim":"knowwledge",
   "Kompyuter":"computer"}

key=input("Enter the word: ")
if key in A:
    print(key, "-",A[key])
else:
    print("The word isn`t in the dictionary")