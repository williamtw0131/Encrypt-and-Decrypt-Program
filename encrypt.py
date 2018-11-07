""" This is a Encrypting and Decrypting Program"""

#Tools we need
import random
import numpy as np

#Program starts here

alphabet = "abcdefghijklmnopqrstuvwxyz"

key = random.randint(0, 27)

encrypted_words = ""

print(key)

words_to_encrypt = input("Please enter the words you want to encrypt: ").lower()

for i in words_to_encrypt:
    
    if i in alphabet:
        
        words_position = alphabet.find(i)

        new_words_position = (words_position + key) % 26

        new_words = alphabet[new_words_position]

        #print(new_words)

        encrypted_words += new_words

        #print(encrypted_words)
        
    else:

        encrypted_words += i

        

print("The new words are: " + encrypted_words)
