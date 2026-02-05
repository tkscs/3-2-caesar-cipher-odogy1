import string

# ----- Some Hints -----
# This will give you a string with all the lowercase letters in the alphabet
alphabet = string.ascii_lowercase


# You can look up the index of a letter in the alphabet like this:
choice = input("Do you want to encrypt, decrypt or did you forget your number?(Encrypt/Decrypt/IDK my number) ")

if choice == "Encrypt":
    plaintext = input("Write your message here: ")
    cra = input("Input a number: ")
    numcra = int(cra)

    # Initialize your ciphertext an empty string
    ciphertext = ""
    for character in plaintext:
        number = ord(character)
        number = number + numcra
        encrypted_character = chr(number) # CHANGE THIS!
        ciphertext += encrypted_character
    print(f"{ciphertext = }")
elif choice == "Decrypt":
    plaintext = input("Write your message here: ")
    cra = input("Input your number: ")
    numcra = int(cra)

    # Initialize your ciphertext an empty string
    ciphertext = ""
    for character in plaintext:
        number = ord(character)
        number = number - numcra
        encrypted_character = chr(number) # CHANGE THIS!
        ciphertext += encrypted_character
    print(f"{ciphertext = }")
elif choice == "IDK my number":
    plaintext = input("Write your message here: ")
    cra = input("Input your minimum number: ")
    cra1 = input("Input your maximum number: ")
    numcraz = int(cra)
    numcra1 = int(cra1)
    numcra1 = numcra1 + 1

    # Initialize your ciphertext an empty string
    for numcra in range(numcraz, numcra1):
        ciphertext = ""
        for character in plaintext:
            number = ord(character)
            number = number - numcra
            encrypted_character = chr(number) # CHANGE THIS!
            ciphertext += encrypted_character
        print(f"{ciphertext = }")