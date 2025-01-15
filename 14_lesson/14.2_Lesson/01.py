import string
while True:
    isleg = int(input('1.To Encrypt\n2.To Decrypt\n3.Exit\nYour Choose: '))
    alphabet = string.ascii_lowercase
    message2 = ""
    if isleg == 1:
        message = input('Enter message: ').lower()
        key = int(input('Enter key: '))
        for i in message:
            if i.isalpha():
                yeri = (alphabet.index(i) + key) % 26
                message2 += alphabet[yeri]
            else:
                message2 += i
        print('ENCRYPTED TEXT: ', message2)
    elif isleg == 2:
        message = input('Enter message: ').lower()
        key = int(input('Enter key: '))
        for i in message:
            if i.isalpha():
                yeri = (alphabet.index(i) - key) % 26
                message2 += alphabet[yeri]
            else:
                message2 += i
        print('DECRYPTED TEXT:', message2)
    elif isleg == 3:
        print('Thanks for using program')
        break
    else:
        print('Wrong command')