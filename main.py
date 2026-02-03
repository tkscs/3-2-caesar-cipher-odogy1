import string

# ----- Some Hints -----
# This will give you a string with all the lowercase letters in the alphabet
alphabet = string.ascii_lowercase


# You can look up the index of a letter in the alphabet like this:
index = alphabet.index("a")
print(f"position of 'a' in the alphabet: {index}")


plaintext = "This is a secret message."

# Initialize your ciphertext an empty string
ciphertext = ""
for character in plaintext:
    # do something to the character to encrypt it
    # YOUR CODE HERE
    encrypted_character = "a" # CHANGE THIS!
    ciphertext += encrypted_character

print(f"{ciphertext = }")