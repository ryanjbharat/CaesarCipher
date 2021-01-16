# Takes a string, turns it uppercase, returns Caesar Cipher of it

# Reference
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    my_index = []  # Get the indexes
    for letter in plaintext:
        if letter in alphabet:
            my_index.append(alphabet.index(letter))
        else:
            my_index.append(letter)

    # Apply the key
    my_index[:] = [x + key if isinstance(x, int) == True else x for x in my_index]
    my_index[:] = [x - 26 if isinstance(x, int) == True and x > 25 else x for x in my_index]

    # Convert into encrypted string
    new_message = ""
    for element in my_index:
        if isinstance(element, int):
            new_message += alphabet[element]
        else:
            new_message += element
    return new_message

# Decrypt
def decrypt(plaintext, key):
    plaintext = plaintext.upper()
    my_index = []
    for letter in plaintext:
        if letter in alphabet:
            my_index.append(alphabet.index(letter))
        else:
            my_index.append(letter)

    # Apply the key
    my_index[:] = [x - key if isinstance(x, int) == True else x for x in my_index]

    # Convert into encrypted string
    new_message = ""
    for element in my_index:
        if isinstance(element, int):
            new_message += alphabet[element]
        else:
            new_message += element
    return new_message


# User input
while True:
    try:
        key = int(input("Enter the key: "))  # Gets the key
        break
    except ValueError:
        print("Not an integer")
user_message = input("Please enter your message: ")  # Gets the message
choice = input("Encode Or Decode: ")  # Gets user choice

if choice.upper() == "ENCODE":
    print(encrypt(user_message, key))
elif choice.upper() == "DECODE":
    print(decrypt(user_message, key))

