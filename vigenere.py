import itertools
import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cipher = []
pos_key = []
pos_text = []
pos_cipher = 0
key = []
plain = []
letters_len = len(letters)


def find_pos(value) :
    temp = []
    i=0
    while i<len(value) :
        j=0
        while j<letters_len:
            if value[i] == letters[j] :
                temp.append(j)
            j = j+1
        i= i+1
    print(temp)
    return temp
        

def vigenere_encrypt_decrypt(n) : 
    K = input("Enter The Key : ")
    P = input("Enter The String to encrypt or decrypt : ")

    key = str.lower(K)
    plain = str.lower(P)
    pos_key = find_pos(key)
    pos_text = find_pos(plain)                                      
    
    if len(pos_key) > len(pos_text) :
            range_list = pos_key
    else :
            range_list = pos_text

    i=0
    j=0
    loop_pass = 0
    
    while i<len(range_list) and j<len(range_list) and loop_pass<len(pos_text) :      
        try :
            pos_cipher = n*pos_key[i] + pos_text[j]

            pos_cipher = pos_cipher % letters_len
            cipher.append(letters[pos_cipher])

            i = i+1
            j = j+1
            
            if i==len(pos_key) and j<len(pos_text) :
                i=0
            elif j==len(pos_text) and i<len(pos_key) :
                j=0

            loop_pass = loop_pass + 1
        except:
            print("Oops Something went wrong")
    
    result = "".join(cipher)
    print(str.upper(result))


def full_vigenere(n) :
    vigenere_square = []
    

def auto_key_vigenere(n) : 
    K = input("Enter The Key : ")
    P = input("Enter The String to encrypt or decrypt : ")

    key = str.lower(K)
    plain = str.lower(P)
    pos_key = find_pos(key)
    pos_text = find_pos(plain)                                      
    
    if ((len(pos_key) < len(pos_text)) and n == 1) :
        pos_key = pos_key + pos_text
    
    range_list = pos_text

    i=0
    j=0

    while i<len(range_list)  :      
        try :
            pos_cipher = n*pos_key[i] + pos_text[j]

            print("pos_cipher", pos_cipher)

            pos_cipher = pos_cipher % letters_len
            cipher.append(letters[pos_cipher])

            if (len(pos_key) < len(range_list)) :
                pos_key.append(pos_cipher)

            i = i+1
            j = j+1
            
        except:
            print("Oops Something went wrong")
    
    result = "".join(cipher)
    print(str.upper(result))



if __name__=='__main__':
    print("1 : Vigenere Standard, 2 : Full Vigenere, 3 : Auto-key Vigenere, 4 : Super Enkripsi")

    vigenere_type = int(input("Enter Vigenere Type :"))

    if (vigenere_type == 1) :
        print("1 : encryp, -1 : decrypt")
        type = int(input("Type : "))
        if (type == 1 or -1) :
            vigenere_encrypt_decrypt(type)
        else :
            print("Oops Something went wrong")
    elif (vigenere_type == 2) :
        pass
    elif (vigenere_type == 3) :
        print("1 : encryp, -1 : decrypt")
        type = int(input("Type : "))
        if (type == 1 or -1) :
            auto_key_vigenere(type)
        else :
            print("Oops Something went wrong")
    elif (vigenere_type == 4) :
        print("1 : encryp, -1 : decrypt")
        type = int(input("Type : "))
        if (type == 1 or -1) :
            vigenere_encrypt_decrypt(type)
        else :
            print("Oops Something went wrong")
    else:
        print("Oops Something went wrong")
    

    
