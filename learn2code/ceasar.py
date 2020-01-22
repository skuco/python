key = int(input('Set the encript key: '))
action = input('Select [e]ncript, or [d]ecript: ')
data = input('Enter the message: ')

if action == 'e':
    text = ''
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord += key # encription
            char_ord %= 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("Encripted text: '{}'".format(text))
    
elif action == 'd':
    text = ''
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord -= key # decription
            char_ord %= 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("Decripted text: '{}'".format(text))
    
else:
    print('Wrong choice!')
