# shift encryptor / decryptor
# lowercase converted
# period and space ignored
# very inelegant solution - will make a better solution (maybe)

def encrypt():
    print('This converter only allows lowercase letters with spaces and periods')
    print('Enter key:')
    key = int(input())
    print('Enter plaintext:')
    plaintext = input()
    print('Ciphertext:')
    print(encode(key, plaintext))

def decrypt():
    print('This converter only allows lowercase letters with no special characters')
    print('Enter key:')
    key = int(input())
    print('Enter ciphertext:')
    ciphertext = input()
    print('Plaintext:')
    print(decode(key, ciphertext))

def encode(key, plaintext):
    length = len(plaintext)
    ciphertext = ''
    for x in range(length):
        if plaintext[x] == ' ':
            ciphertext = ciphertext + ' '
        elif plaintext[x] == '.':
            ciphertext = ciphertext + '.'
        else:
            ciphertext = ciphertext + encodeCharacter(key, plaintext[x])
    return ciphertext

def decode(key, ciphertext):
    length = len(ciphertext)
    plaintext = ''
    for x in range(length):
        if ciphertext[x] == ' ':
             plaintext = plaintext + ' '
        elif ciphertext[x] == '.':
             plaintext = plaintext + '.'
        else:
            plaintext = plaintext + decodeCharacter(key, ciphertext[x])
    return plaintext

def encodeCharacter(key, letter):
    letterValue = getValue(letter)
    newValue = (letterValue + key) % 26
    return getLetter(newValue)

def decodeCharacter(key, letter):
    letterValue = getValue(letter)
    newValue = (letterValue - key) % 26
    return getLetter(newValue)

def getValue(letter):
    if letter == 'a':
        return 0
    elif letter == 'b':
        return 1
    elif letter == 'c':
        return 2
    elif letter == 'd':
        return 3
    elif letter == 'e':
        return 4
    elif letter == 'f':
        return 5
    elif letter == 'g':
        return 6
    elif letter == 'h':
        return 7
    elif letter == 'i':
        return 8
    elif letter == 'j':
        return 9
    elif letter == 'k':
        return 10
    elif letter == 'l':
        return 11
    elif letter == 'm':
        return 12
    elif letter == 'n':
        return 13
    elif letter == 'o':
        return 14
    elif letter == 'p':
        return 15
    elif letter == 'q':
        return 16
    elif letter == 'r':
        return 17
    elif letter == 's':
        return 18
    elif letter == 't':
        return 19
    elif letter == 'u':
        return 20
    elif letter == 'v':
        return 21
    elif letter == 'w':
        return 22
    elif letter == 'x':
        return 23
    elif letter == 'y':
        return 24
    elif letter == 'z':
        return 25
    else:
        return 'error'

def getLetter(value):
    if value == 0:
        return 'a'
    elif value == 1:
        return 'b'
    elif value == 2:
        return 'c'
    elif value == 3:
        return 'd'
    elif value == 4:
        return 'e'
    elif value == 5:
        return 'f'
    elif value == 6:
        return 'g'
    elif value == 7:
        return 'h'
    elif value == 8:
        return 'i'
    elif value == 9:
        return 'j'
    elif value == 10:
        return 'k'
    elif value == 11:
        return 'l'
    elif value == 12:
        return 'm'
    elif value == 13:
        return 'n'
    elif value == 14:
        return 'o'
    elif value == 15:
        return 'p'
    elif value == 16:
        return 'q'
    elif value == 17:
        return 'r'
    elif value == 18:
        return 's'
    elif value == 19:
        return 't'
    elif value == 20:
        return 'u'
    elif value == 21:
        return 'v'
    elif value == 22:
        return 'w'
    elif value == 23:
        return 'x'
    elif value == 24:
        return 'y'
    elif value == 25:
        return 'z'
    else:
        return 777
    
    
loop = True

while loop:

    print('Would you like to encryt or decrypt?')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Exit')

    answer = input()

    if answer == '1':
        encrypt()
    elif answer == '2':
        decrypt()
    else:
        loop = False

