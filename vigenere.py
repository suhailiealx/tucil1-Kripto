import os

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cipher = []
pos_key = []
pos_text = []
pos_cipher = 0
key = []
plain = []
letters_len = len(letters)


def find_pos(value):
    temp = []
    i=0
    while i<len(value):
        j=0
        while j<letters_len:
            if value[i] == letters[j]:
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
    
    print(key)
    print(plain)

    if len(pos_key) > len(pos_text):
            range_list = pos_key
    else :
            range_list = pos_text
    i=0
    j=0
    loop_pass = 0
    
    while i<len(range_list) and j<len(range_list) and loop_pass<len(pos_text):      
        try:
            pos_cipher = n*pos_key[i] + pos_text[j]
            if pos_cipher<letters_len:
                cipher.append(letters[pos_cipher])
            else:
                pos_cipher = pos_cipher % letters_len
                cipher.append(letters[pos_cipher])

            i = i+1
            j = j+1
            
            if i==len(pos_key) and j<len(pos_text):
                i=0
            elif j==len(pos_text) and i<len(pos_key):
                j=0

            loop_pass = loop_pass + 1
        except:
            print("Oops Something went wrong")
    
    result = "".join(cipher)
    print(str.upper(result))


if __name__=='__main__':
    print("1 : encryp, -1 : decrypt")
    type = int(input("Type : "))
    if (type == 1 or -1) :
        vigenere_encrypt_decrypt(type)
    else :
        print("Oops Something went wrong")
