komp = input('Enter the string: ')
letters = 0
cap_letters = 0
smail_letters = 0
digits = 0
spaces = 0
for letter in komp:
    if letter.isalpha():
        letters += 1
        if letter.isupper():
            cap_letters += 1
        elif letter.islower():
            smail_letters += 1
    elif letter.isdigit():
        digits += 1
    else:
        spaces += 1
print(f'letters: {letters}')
print(f'capital letters: {cap_letters}')
print(f'smail letters: {smail_letters}')
print(f'Digits: {digits}')
print(f'Spaces: {spaces}')