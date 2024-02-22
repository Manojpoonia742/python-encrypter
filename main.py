import base64


def dev():
    choice = input('Enter your choice:E for Encrypt , D for Decrypt :').lower()
    if choice == 'e':
        password = input('Enter password you want to encrypt : ')
        encpassword = base64.b64encode(password.encode())
        print(encpassword)
    elif choice == 'd':
        enckey = input('Enter key you want to decrypt : ')
        decpassword = base64.b64decode(enckey)
        print(decpassword)
    else:
        print('You typed a wrong input')
        dev()


dev()
