
dictionary = {
    'hello': 'salam',
    'apple': 'alma',
    'lemon': 'limon',
    'cat': 'pisik',
    'dog': 'it',
    'Flag': 'baydak',
    'student': 'okuwcy',
    'family': 'masgala',
    'pen': 'ruçka',
    'water': 'suw',
    'bread': 'çörek'
}

while True:
    print("\n*My Dictionary Program*")
    print("1. Show")
    print("2. Add")
    print("3. Edit")
    print("4. Delete")
    print("5. Exit")
    choice = input("Your choice? ")

    if choice == '1': 
        if dictionary:
            print("\nSözlükdäki sözler:")
            for word, translation in dictionary.items():
                print(f"{word} - {translation}")
        else:
            print("Sözlük boş!")

    elif choice == '2':  
        english = input("Enter the word in English: ").strip()
        turkmen = input("Enter the word in Türkmen: ").strip()
        if english and turkmen:
            dictionary[english] = turkmen
            print("Added successfully!")
        else:
            print("Düzgünli söz giriziň!")

    elif choice == '3':  
        english = input("Enter the word in English to edit: ").strip()
        if english in dictionary:
            turkmen = input("Enter the new word in Türkmen: ").strip()
            if turkmen:
                dictionary[english] = turkmen
                print("Edited successfully!")
            else:
                print("Düzgünli söz giriziň!")
        else:
            print("Söz tapylmady!")

    elif choice == '4': 
        english = input("Enter the word in English to delete: ").strip()
        if english in dictionary:
            del dictionary[english]
            print("Deleted successfully!")
        else:
            print("Söz tapylmady!")

    elif choice == '5':  
        print("Thanks for using the program. Goodbye!")
        break

    else:  
        print("Wrong command...")
        break