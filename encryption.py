import sys
from cs50 import get_string





def encryption():
    key = get_string("key: ")
    length_key = len(key)


    for i in range(length_key):
        if key[i] == " ":
            print("Usage: key")
            return 1

        elif (len(key) != 26):
            print("Key must contain 26 characters.")
            return 1

    if not key.isalpha():
        print("Usage: key2")
        return 1

    for i in range(length_key):
        for j in range(i + 1,length_key):
            if str(key[i]).upper() == str(key[j]).upper():
                print("Usage: key3")
                return 2

    plaintext = get_string("plaintext: ")
    length_pt = len(plaintext)
    print("ciphertext: ")

    for i in range(length_key):
        if str(key[i]).islower() == True:
            key[i] = key[i] - 32

    for i in range(length_pt):
        if str(plaintext[i]).isupper() == True:
            l = ord(plaintext[i]) - 65
            print(key[l], end="")
        elif str(plaintext[i]).islower() == True:
            l = ord(plaintext[i]) - 97
            ll = ord(key[l]) + 32
            print(chr(ll), end="")
        else:
            print(plaintext[i], end="")
    print()


if __name__ == "__main__":
    encryption()