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
ascii_len = 256
vigenere_square = []


def reset_variable() :
    cipher = []
    pos_key = []
    pos_text = []
    pos_cipher = 0
    key = []
    plain = []


def find_pos(value) :
    temp = []
    i=0
    while i<len(value) :
        j=0
        while j<letters_len:
            if value[i] == letters[j] :
                temp.append(j)
                break
            j = j+1
        i= i+1
    print(temp)
    return temp


def find_pos_ascii(value) :
    temp = []
    i=0
    while i<len(value) :
        temp.append(ord(value[i]))
        i = i+1
    print(temp)
    return temp
        

def find_pos_full(value) :
    temp = []
    i=0
    while i<len(value) :
        j=0
        while j<letters_len:
            if value[i] == letters[j] :
                temp.append(j)
                break
            j = j+1
        i= i+1
    print(temp)
    return temp


def rand_full_vigenere_square() :
    vigenere_square.clear()
    for _ in range(0, letters_len) :
        vigenere_square.append(random.sample(letters, letters_len))
    print("Full vigenere square berhasil di reset")




def vigenere(n, K, P) : 
    cipher = []
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
    return(str.upper(result))


def full_vigenere(n, K, P) :
    cipher = []
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
    
    if (n == 1) :
        while i<len(range_list) and j<len(range_list) and loop_pass<len(pos_text) :      
            try :
                print(vigenere_square)
                print("pos_key : ", pos_key[i])
                print("pos_text : ", pos_text[j])
                aa = vigenere_square[pos_key[i]][pos_text[j]]
                cipher.append(aa)

                i = i+1
                j = j+1
                
                if i==len(pos_key) and j<len(pos_text) :
                    i=0
                elif j==len(pos_text) and i<len(pos_key) :
                    j=0

                loop_pass = loop_pass + 1
                    
            except:
                print("Oops Something went wrong")
    
    elif (n == -1) :
        while i<len(range_list) and j<len(range_list) and loop_pass<len(pos_text) :      
            try :
                pos_cipher = vigenere_square[pos_key[i]].index(letters[pos_text[j]])
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
    return(str.upper(result))


def auto_key_vigenere(n, K, P) : 
    cipher = []
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

            pos_cipher = pos_cipher % letters_len
            cipher.append(letters[pos_cipher])

            if (len(pos_key) < len(range_list)) :
                pos_key.append(pos_cipher)

            i = i+1
            j = j+1
            
        except:
            print("Oops Something went wrong")
    
    result = "".join(cipher)
    return(str.upper(result))


def extended_vigenere(n, K, P) : 
    cipher = []
    pos_key = find_pos_ascii(K)
    pos_text = find_pos_ascii(P)                                      
    
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

            pos_cipher = pos_cipher % ascii_len
            cipher.append(chr(pos_cipher))

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
    print(result)
    return(result)


def super_enkripsi(n, K, P) :
    cipher = []
    if (n == 1) :
        first_enkripsi = vigenere(n, K, P)
        return (transposisi(n, first_enkripsi))
    elif (n == -1) :
        first_dekripsi = transposisi(n, P)
        return (vigenere(n, K, first_dekripsi))


def transposisi(n, text) :
    cipher = []
    text = str.lower(text)

    if (n == 1) :
        arr0 = []
        arr1 = []

        for i in range(0, len(text)) :
            if (i % 2 == 0) :
                arr0.append(text[i])
            else:
                arr1.append(text[i])
            
        arr = arr0 + arr1

        result = "".join(arr)
        return(str.upper(result))

    elif (n == -1) :
        center = len(text) // 2

        print("text : ", text)
        if (len(text) % 2 == 0) :
            arr0 = text[:center]
            arr1 = text[center:]

        else :
            arr0 = text[:center+1]
            arr1 = text[center+1:]
        
        arr = []
        max_len = 0
        if (len(text) % 2 == 0) :
            max_len = center
        else:
            max_len = center + 1

        for i in range(0, max_len) :
            if (i < len(arr0)) :
                arr.append(arr0[i])
            if (i < len(arr1)) :
                arr.append(arr1[i])

        result = "".join(arr)
        return(str.upper(result))




if __name__=='__main__':
    rand_full_vigenere_square()

    ss = vigenere_square
    for i in range (len(vigenere_square)) :
        print(vigenere_square[i])
    
    while (True) :

        reset_variable()
        print("1 : Vigenere Standard, 2 : Full Vigenere, 3 : Auto-key Vigenere, 4 : Extended Vigenere, 5 : Super Enkripsi")
        vigenere_type = int(input("Enter Vigenere Type : "))

        print("1 : encryp, -1 : decrypt")
        type = int(input("Type : "))

        K = input("Enter The Key : ")
        P = input("Enter The String to encrypt or decrypt : ")

        if (vigenere_type != 4) :
            K = K.replace(" ", "")
            P = P.replace(" ", "")

        if (type == 1 or -1) :
            if (vigenere_type == 1) :
                print(vigenere(type, K, P))
            elif (vigenere_type == 2) :
                print(full_vigenere(type, K, P))
            elif (vigenere_type == 3) :
                print(auto_key_vigenere(type, K, P))
            elif (vigenere_type == 4) :
                print(extended_vigenere(type, K, P))
            elif (vigenere_type == 5) :
                print(super_enkripsi(type, K, P))
            else :
                print("Oops Something went wrong")
        else :
            print("Oops Something went wrong")