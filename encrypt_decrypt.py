
""" This is a Encrypting and Decrypting Program"""

#Tools we need : random

#Program starts here

# creat both upper and lower to make the words stay original
alphabet = "abcdefghijklmnopqrstuvwxyz"
Alphabet = alphabet.upper()
while True:
    import random
    import numpy as np

    print("This is a Encrypt and Decrypt Program.")
    print("======================================")
    print("Please read the following instruction.")
    print("Enter < ecp > to encrypt.")
    print("Enter < dcp > to decrypt.")
    print("Enter < quit > to quit this program")

    user_input = input("Please enter your request: ")

    if user_input == "quit":
        break

    elif user_input == "ecp":
        # get a key for encryption
        key = random.randint(54, 297) # any weird number will do

        encrypted_words = ""

        # ask for the words for encryptiion
        words_to_encrypt = input("Please enter the words you want to encrypt: ").lower()

        # iterate through the words
        for i in words_to_encrypt:

            if i in alphabet:
                words_position = alphabet.find(i) # find the position of each word in alphabet string
                new_words_position = (words_position + key) % 26 # encrypt method is move the position by "key" steps
                new_words = alphabet[new_words_position] # the position after encryption
                encrypted_words += new_words # store the letter

            elif i in Alphabet:
                words_position = Alphabet.find(i)
                new_words_position = (words_position + key) % 26
                new_words = Alphabet[new_words_position]
                encrypted_words += new_words

            else:
                # if it is a space or a , or something else than a letter, just keep it
                encrypted_words += i
        print(f"The new words are: {encrypted_words} and this is your key to decrypt: {key}")

    elif user_input == "dcp":

        # check for the right key input which must be a interger
        try:
            key = int(input("Please enter your key to decrytp: "))
        except ValueError:
            print("Are you sure you have the key?")
            continue
        else:
            decrypted_words = ""
            words_to_decrypt = input("Please enter the words you want to decrypt: ")

            # iterate through the words
            for i in words_to_decrypt:

                if i in alphabet:
                    words_position = alphabet.find(i) # find the decrypt position
                    org_position = (words_position - key) % 26 # move it back with the key
                    org_words = alphabet[org_position]
                    decrypted_words += org_words # store the letter

                elif i in Alphabet:
                    words_position = Alphabet.find(i)
                    org_position = (words_position - key) % 26
                    org_words = Alphabet[org_position]
                    decrypted_words += org_words

                else:
                    decrypted_words += i
            print(f"With the key {key} you given, the original words are: {decrypted_words}")

    else:
        print("Invalid request!!!")
