# Dictionary Program

# Create an empty dictionary to store words
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
    'bread': 'görek'
}

# Function to display the dictionary
def show_words():
    print("\n*My Dictionary*")
    for word, translation in dictionary.items():
        print(f"{word} - {translation}")

# Function to add a new word
def add_word():
    english_word = input("Enter the word in English: ")
    turkmen_word = input(f"Enter the word in Türkmen for '{english_word}': ")
    dictionary[english_word] = turkmen_word
    print("Added successfully")

# Function to edit an existing word
def edit_word():
    english_word = input("Enter the word in English to edit: ")
    if english_word in dictionary:
        turkmen_word = input(f"Enter the new word in Türkmen for '{english_word}': ")
        dictionary[english_word] = turkmen_word
        print("Edited successfully")
    else:
        print("Word not found.")

# Function to delete a word
def delete_word():
    english_word = input("Enter the word in English to delete: ")
    if english_word in dictionary:
        del dictionary[english_word]
        print("Deleted successfully")
    else:
        print("Word not found.")

# Main program loop
while True:
    print("\n*My Dictionary Program*")
    print("1. Show")
    print("2. Add")
    print("3. Edit")
    print("4. Delete")
    print("5. Exit")
    choice = input("Your choice? ")

    if choice == '1':
        show_words()
    elif choice == '2':
        add_word()
    elif choice == '3':
        edit_word()
    elif choice == '4':
        delete_word()
    elif choice == '5':
        print("Thanks for using Program :)")
        break
    else:
        print("Sorry, but we cannot complete this task :(")

