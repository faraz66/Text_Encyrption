# importing numpy library
import numpy as np


# Transposition Cipher Function
def transposition(string):
    print('\n[TRANSPOSITION CIPHER]')
    # taking the key input for transposition cipher
    key = int(input('Select the key:\n1.Reverse\n2.Even Odd\nYour Choice: '))
    # if else for each key type
    if key == 1:
        string = string[::-1]  # reversing the string
    elif key == 2:
        str1 = string[::2]  # Even indexes
        str2 = string[1::2]  # Reversed Odd indexes
        string = str1 + str2  # add even+odd(reversed)
    # returning results
    return string, key


# Transpositon decryption function
def transposition_decrypt(encrypted, key):
    # check the key type
    if key == 1:  # key for reverse
        text = encrypted[::-1]
    else:  # key will be for even odd
        # divide into half i.e. even and odd
        divide = len(encrypted)//2
        # store into even-odd strings
        te = encrypted[:-divide]
        to = encrypted[-divide:]
        # uncomment for debugging
        # print(to, te, len(encrypted)//2)
        # initialize iteration variables
        i = 0
        j = 0
        # declare the text string
        text = ''
        # loop to get the proper text from even and odd
        for k in range(len(encrypted)):
            if k % 2 == 0:  # if even
                text += te[i]  # get char from even-string
                i += 1
            else:  # if odd
                text += to[j]  # get char from odd-string
                j += 1
    # return the final obtained text
    return text


# function for shift cipher
def shift(string):
    # list to store ascii values of characters
    ascii_list =[]
    print('\n[SHIFT CIPHER]')
    key = int(input("Enter The Key: "))  # getting the key
    for i in string:  # converting the characters to 0-255
        # using ord to get ascii values
        ascii_list.append(ord(i))  # -65)  # add to the list we made
    # covert to np array and add key, the mod 256
    # using numpy because it save you from manually coding
    ascii_list = (np.array(ascii_list) + key) % 256

    char_list = []  # list for storing chars
    for i in ascii_list:
        # chr to get char from ascii value
        char_list.append(chr(i))

    # logic from converting list to string
    cipher_text = ''
    for char in char_list:
        cipher_text += char

    print(f'[RESULT OF SHIFT]: {cipher_text}')
    return cipher_text, key  # returning results


# Decryption function for shift cipher
def shift_decrypt(ciphered_text, key):
    ascii_list = []
    for i in ciphered_text:  # converting the characters to 0-255
        # using ord to get ascii values
        ascii_list.append(ord(i))  # add to the list we made
    # covert to np array and add 256, subtract key, then mod 256
    ascii_list = (np.array(ascii_list) + 256 - key) % 256
    # loop for converting the numeric values to their characters
    text = ''
    for char in ascii_list:
        text += chr(char)
    return text


# main function in python
if __name__ == "__main__":
    # open the file, using f as file pointer in write mode
    f = open('data.txt', 'w')
    # got the input
    print('[MAIN INPUT]')
    message = input('Enter the message: ')
    f.write(message)  # write to file
    f.close()  # close the file
    # function call for ciphers
    cipher, shiftKey = shift(message)
    cipher, transKey = transposition(cipher)
    # open the file, using f as file pointer in write mode
    f = open('data.txt', 'w', encoding='utf-8')
    f.write(cipher)  # write to file
    print(f'\n[CIPHERED TEXT] {cipher}')
    f.close()  # close the file

    # Decrypting Section
    print('\n[DECIPHER INPUT]')
    # get the input for decryption
    # 0 for no, 1 for yes
    decrypt = int(input('Would you like to decipher [0/1]: '))
    if decrypt == 0:
        exit(0)  # if no, then exit
    # else open the file in read mode
    f = open('data.txt', 'r', encoding='utf-8')
    cipher = str(f.readline())  # readline from the file
    f.close()  # close file pointer
    # call the decryption function for transposition
    plain_text = transposition_decrypt(cipher, transKey)
    # call the decryption function for shift cipher
    plain_text = shift_decrypt(plain_text, shiftKey)
    # print the deciphered text
    print(f'\n[DECIPHERED TEXT] {plain_text}')
    f = open('data.txt', 'w')
    f.write(plain_text)
    f.close()
