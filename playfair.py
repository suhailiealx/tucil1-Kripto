plaintext = ""
ciphertext = ""
type_plaintext = 0

#For grouping 5 character from a string
def fiveGroup(string, length):
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))

#Playfair Cipher Function
playfair_key_matrix = [ [ 0 for i in range(5) ] for j in range(5) ]
playfair_key = ""
playfair_bigram_list = []

def generateKeyMatrixPlayfair(playfair_key_matrix, playfair_key) :
    alphabet = "abcdefghiklmnopqrstuvwxyz"

    playfair_key = playfair_key.replace(' ', '').replace('j','').replace('J','')
    playfair_key = ''.join([j for i,j in enumerate(playfair_key) if j not in playfair_key[:i]])

    for i,k in enumerate(alphabet) :
        if (k) not in playfair_key :
            playfair_key = playfair_key + k

    l = [list(playfair_key[i:i+5]) for i in range(0, len(playfair_key), 5)]
    playfair_key_matrix = [s if len(s) == 5 else s+[None]*(5-len(s)) for s in l]
        
    return playfair_key_matrix

def encryptPlayfair(plaintext, ciphertext, playfair_key) :

    playfair_key_matrix = [ [ 0 for i in range(5) ] for j in range(5) ]
    playfair_bigram_list = []

    plaintext = plaintext.replace(' ','').replace('j','i').replace('J','I').replace('!','').replace('.','').replace('/','').replace('?','')
    playfair_key_matrix = generateKeyMatrixPlayfair(playfair_key_matrix,playfair_key)

    i=0
    playfair_bigram_list = []

    len_plaintext = len(plaintext)

    while (i <= len_plaintext-1) :
        if ((i+1) <= len(plaintext)-1) :
            bigram = plaintext[i:i+2]
            if (bigram[0] == bigram[1]) :
                bigram = bigram[:1] + 'x' + bigram[1+1:]
                i = i+1
                len_plaintext = len_plaintext+1
            else :
                i = i+2
        else :
            bigram = plaintext[-1] + 'x'
            i = i+2
        
        playfair_bigram_list.append(bigram)
    
    ciphertext = ""

    for i,k in enumerate(playfair_bigram_list) :
        index_first = [(index, row.index(k[0])) for index, row in enumerate(playfair_key_matrix) if k[0] in row]
        index_second = [(index, row.index(k[1])) for index, row in enumerate(playfair_key_matrix) if k[1] in row]

        #Case 1, terdapat pada baris yang sama
        if (index_first[0][0] == index_second[0][0]) :
            bigram_cipher = playfair_key_matrix[index_first[0][0]][(index_first[0][1] + 1) % 5] + playfair_key_matrix[index_second[0][0]][(index_second[0][1] + 1 ) % 5]
        
        #Case 2, terdapat pada kolom yang sama
        elif (index_first[0][1] == index_second[0][1]) :
            bigram_cipher = playfair_key_matrix[(index_first[0][0] + 1) % 5][index_first[0][1]] + playfair_key_matrix[(index_second[0][0] + 1 ) % 5][index_second[0][1]]

        #Case 3, terdapat pada kolom atau baris yang berbeda
        else :
            bigram_cipher = playfair_key_matrix[index_first[0][0]][index_second[0][1]] + playfair_key_matrix[index_second[0][0]][index_first[0][1]]

        ciphertext = ciphertext + bigram_cipher.upper()
    
    return ciphertext

def decryptPlayfair(plaintext, ciphertext, playfair_key) :

    i=0
    playfair_key_matrix = [ [ 0 for i in range(5) ] for j in range(5) ]
    playfair_bigram_list = []

    playfair_key_matrix = generateKeyMatrixPlayfair(playfair_key_matrix,playfair_key)

    while (i < len(ciphertext)) :
        bigram_cipher = ciphertext[i:i+2]
        playfair_bigram_list.append(bigram_cipher.lower())
        i = i+2

    print(playfair_bigram_list)
    plaintext = ""

    for i,k in enumerate(playfair_bigram_list) :

        index_first = [(index, row.index(k[0])) for index, row in enumerate(playfair_key_matrix) if k[0] in row]
        index_second = [(index, row.index(k[1])) for index, row in enumerate(playfair_key_matrix) if k[1] in row]

        #Case 1, terdapat pada baris yang sama
        if (index_first[0][0] == index_second[0][0]) :
            bigram_cipher = playfair_key_matrix[index_first[0][0]][(index_first[0][1] - 1) % 5] + playfair_key_matrix[index_second[0][0]][(index_second[0][1] - 1 ) % 5]
        
        #Case 2, terdapat pada kolom yang sama
        elif (index_first[0][1] == index_second[0][1]) :
            bigram_cipher = playfair_key_matrix[(index_first[0][0] - 1) % 5][index_first[0][1]] + playfair_key_matrix[(index_second[0][0] - 1 ) % 5][index_second[0][1]]

        #Case 3, terdapat pada kolom atau baris yang berbeda
        else :
            bigram_cipher = playfair_key_matrix[index_first[0][0]][index_second[0][1]] + playfair_key_matrix[index_second[0][0]][index_first[0][1]]

        print(bigram_cipher)
        plaintext = plaintext + bigram_cipher

    plaintext = plaintext.replace('x','')

    return plaintext
        
#Affine Cipher Function
m_prime = 0
b_shift = 0

def encryptAffine(plaintext, ciphertext, m_prime, b_shift) :
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    ciphertext = ""

    for i in range(len(plaintext)) :
        index = (m_prime * alphabet.find(plaintext[i]) + b_shift) % 26
        cipher_letter = alphabet[index]

        ciphertext = ciphertext + cipher_letter.upper()    
    
    return ciphertext

def decryptAffine(plaintext, ciphertext, m_prime, b_shift) :
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    plaintext = ""

    m_inverse = 0
    for i in range(1,26) :
        if ((m_prime * i) % 26) == 1 :
            m_inverse = i
            break
    
    for i in range(len(ciphertext)) :
        index = (m_inverse * (alphabet.find(ciphertext[i].lower()) - b_shift)) % 26
        plain_letter = alphabet[index]

        plaintext = plaintext + plain_letter.lower()    

    return plaintext

#Hill Cipher Function
hill_key = [ [ 0 for i in range(3) ] for j in range(3) ]
hill_trigram_list = []

def encryptHill(plaintext, ciphertext, hill_key) :
    i=0
    matrix_process = []
    hill_key_int = [ [ 0 for i in range(3) ] for j in range(3) ]
    sum = 0

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = plaintext.replace(' ','')

    for i in range(len(hill_key_int)) :
        for j in range(len(hill_key_int[0])) :
            hill_key_int[i][j] = int(hill_key[(i*2)+j+i])


    i=0
    while (i < len(plaintext)) :
        trigram = plaintext[i:i+3]
        i = i+3
        hill_trigram_list.append(trigram)

    for x in range(len(hill_trigram_list)) :
        for i in range(len(hill_trigram_list[x])) :
            for j in range(len(hill_trigram_list[x])) :
                sum = sum + (hill_key_int[i][j] * alphabet.index(hill_trigram_list[x][j]))
            matrix_process.append(sum)
            sum = 0
        for k in range(len(matrix_process)) :
            matrix_process[k] = matrix_process[k] % 26
            ciphertext = ciphertext + alphabet[matrix_process[k]].upper()
            print(ciphertext)

        matrix_process = []
    
    return ciphertext

def decryptHill(plaintext, ciphertext, hill_key) :

    matrix_process = []
    hill_key_int = [ [ 0 for i in range(3) ] for j in range(3) ]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i=0

    for i in range(len(hill_key_int)) :
        for j in range(len(hill_key_int[0])) :
            hill_key_int[i][j] = int(hill_key[(i*2)+j+i])
    print(hill_key_int)

    i=0
    while (i < len(ciphertext)) :
        trigram = ciphertext[i:i+3]
        i = i+3
        hill_trigram_list.append(trigram)

    print(hill_trigram_list)
    for x in range(len(hill_trigram_list)) :
        key_matrix_not_inverse = [[ 0 for i in range(len(hill_trigram_list[x])) ] for j in range(len(hill_trigram_list[x]))]
        key_matrix_inverse = [[ 0 for i in range(len(hill_trigram_list[x])) ] for j in range(len(hill_trigram_list[x]))]

        for i in range(len(hill_trigram_list[x])) :
            for j in range(len(hill_trigram_list[x])) :
                key_matrix_not_inverse[i][j] = hill_key_int[i][j]

    key_matrix_inverse = generateMatrixInverse(key_matrix_not_inverse)

    plaintext = ""
    sum = 0

    for x in range(len(hill_trigram_list)) :
        for i in range(len(hill_trigram_list[x])) :
            for j in range(len(hill_trigram_list[x])) :
                sum = sum + (key_matrix_inverse[i][j] * alphabet.index(hill_trigram_list[x][j].lower()))
            matrix_process.append(sum)
            sum = 0
        for k in range(len(matrix_process)) :
            matrix_process[k] = matrix_process[k] % 26
            plaintext = plaintext + alphabet[matrix_process[k]]
            print(plaintext)

        matrix_process = []
    
    return plaintext

def generateMatrixInverse(matrix) :

    if len(matrix[0]) == 1 :
        matrix[0][0] = 1/matrix[0][0]
    elif len(matrix[0]) == 2 :
        determinant = generateDeterminant(matrix,2)

        temp = matrix[0][0]
        matrix[0][0] = matrix[1][1]
        matrix[1][1] = temp
        matrix[0][1] = -(matrix[0][1])
        matrix[1][0] = -(matrix[1][0])

        m_inverse = 0
        for i in range(1,26) :
            if ((determinant * i) % 26) == 1 :
                m_inverse = i
                break

        for i in range(2) :
            for j in range(2) :
                matrix[i][j] = (matrix[i][j]*m_inverse) % 26

        return matrix
    
    else :
        determinant = generateDeterminant(matrix,3)

        matrix_i = [[ 0 for i in range(3) ] for j in range(3)]
        matrix_i[0][0] = matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2]
        matrix_i[0][1] = -(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
        matrix_i[0][2] = matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]
        matrix_i[1][0] = -(matrix[0][1]*matrix[2][2] - matrix[2][1]*matrix[0][2])
        matrix_i[1][1] = matrix[0][0]*matrix[2][2] - matrix[0][2]*matrix[2][0]
        matrix_i[1][2] = -(matrix[0][0]*matrix[2][1] - matrix[0][1]*matrix[2][0])
        matrix_i[2][0] = matrix[0][1]*matrix[1][2] - matrix[1][1]*matrix[0][2]
        matrix_i[2][1] = -(matrix[0][0]*matrix[1][2] - matrix[0][2]*matrix[1][0])
        matrix_i[2][2] = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

        matrix_i_t = [[ 0 for i in range(3) ] for j in range(3)]

        for i in range(len(matrix_i)) :
            for j in range(len(matrix_i[0])) :
                matrix_i_t[j][i] = matrix_i[i][j]

        m_inverse = 0
        for i in range(1,26) :
            if ((determinant * i) % 26) == 1 :
                m_inverse = i
                break

        for i in range(3) :
            for j in range(3) :
                matrix_i_t[i][j] = (matrix_i_t[i][j]*m_inverse) % 26

        return matrix_i_t

def generateDeterminant(matrix, length) :

    if length == 2 :
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    elif length == 3 :
        return (matrix[0][0]*((matrix[1][1]*matrix[2][2]) - (matrix[2][1]*matrix[1][2])) - matrix[0][1]*((matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0])) + matrix[0][2]*((matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0])))

if __name__=='__main__':
    
    print("\n1. Playfair Cipher")
    print("2. Affine Cipher")
    print("3. Hill Cipher")
    print("------------")
    choice_cipher = int(input("Your cipher choice : "))

    print("1. Encryption")
    print("2. Decryption")
    choice_crypt = int(input("Your choice : "))

    #Playfair Cipher
    if choice_cipher == 1 :
        if (choice_crypt == 1) :
            plaintext = input("Plain text : ")
            playfair_key = input("Key Encryption : ")
            playfair_key_matrix = generateKeyMatrixPlayfair(playfair_key_matrix,playfair_key)
            ciphertext = encryptPlayfair(plaintext,ciphertext,playfair_key_matrix)
            print(ciphertext)

        else :
            ciphertext = input("Cipher text : ")
            playfair_key = input("Key Decryption : ")
            type_plaintext = int(input("Type of Plaintext : 1. No Space    2. 5-word Group\n"))
            playfair_key_matrix = generateKeyMatrixPlayfair(playfair_key_matrix,playfair_key)
            plaintext = decryptPlayfair(plaintext,ciphertext,playfair_key_matrix)
            if (type_plaintext == 2) :
                print(fiveGroup(plaintext,5))
            else :
                print(plaintext)

    #Affine Cipher
    elif choice_cipher == 2 :
        if (choice_crypt == 1) :
            plaintext = input("Plain text : ")
            m_prime = int(input("Prime number that relatively prime to 26 : "))
            b_shift = int(input("Number of shift : ")) % 26
            ciphertext = encryptAffine(plaintext, ciphertext, m_prime, b_shift)
            print(ciphertext)

        else :
            ciphertext = input("Cipher text : ")
            m_prime = int(input("Prime number that relatively prime to 26 : "))
            b_shift = int(input("Number of shift : "))
            type_plaintext = int(input("Type of Plaintext : 1. No Space    2. 5-word Group\n"))
            plaintext = decryptAffine(plaintext, ciphertext, m_prime, b_shift)
            if (type_plaintext == 2) :
                print(fiveGroup(plaintext,5))
            else :
                print(plaintext)

    #Hill Cipher
    elif choice_cipher == 3 :
        if (choice_crypt == 1) :
            plaintext = input("Plain text : ")
            for i in range(len(hill_key)) :
                for j in range(len(hill_key[0])) :
                    hill_key[i][j] = int(input("Key for the k" + str(i+1) + str(j+1) + " : "))

            ciphertext = encryptHill(plaintext,ciphertext,hill_key)
            print(ciphertext)

        else :
            ciphertext = input("Cipher text : ")
            for i in range(len(hill_key)) :
                for j in range(len(hill_key[0])) :
                    hill_key[i][j] = int(input("Key for the k" + str(i+1) + str(j+1) + " : "))

            plaintext = decryptHill(plaintext,ciphertext,hill_key)
            print(plaintext)