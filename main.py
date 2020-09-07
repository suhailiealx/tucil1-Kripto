from tkinter import *
from vigenere import *
from tkinter import filedialog


# selected_algorithm = 0

class Application(Frame):
    selected_algorithm = 0
    output_type = 0
    filename = ""
    f = ""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.resetSquare()

    def createWidgets(self):
        # RadioButton
        var = IntVar()

        R1 = Radiobutton(root, text="Standard Vigenere Cipher", variable=var, value=1, command = lambda : self.getScript(R1))
        R1.pack( anchor = W )

        R2 = Radiobutton(root, text="Full Vigenere Cipher", variable=var, value=2, command = lambda : self.getScript(R2))
        R2.pack( anchor = W )

        R3 = Radiobutton(root, text="Auto-key Vigenere Cipher", variable=var, value=3, command = lambda : self.getScript(R3))
        R3.pack( anchor = W )

        R4 = Radiobutton(root, text="Extended Vigenere Cipher", variable=var, value=4, command = lambda : self.getScript(R4))
        R4.pack( anchor = W )

        R5 = Radiobutton(root, text="Playfair Cipher", variable=var, value=5, command = lambda : self.getScript(R5))
        R5.pack( anchor = W )

        R6 = Radiobutton(root, text="Super Enkripsi", variable=var, value=6, command = lambda : self.getScript(R6))
        R6.pack( anchor = W )

        R7 = Radiobutton(root, text="Affine Cipher", variable=var, value=7, command = lambda : self.getScript(R7))
        R7.pack( anchor = W )

        R8 = Radiobutton(root, text="Hill Cipher", variable=var, value=8, command = lambda : self.getScript(R8))
        R8.pack( anchor = W )

        R9 = Radiobutton(root, text="Enigma Cipher", variable=var, value=9, command = lambda : self.getScript(R9))
        R9.pack( anchor = W )


        # RadioButton pilihan output
        P1 = Radiobutton(root, text="Tanpa Spasi", value=0, command = lambda : self.getOutputType(P1))
        P1.pack( anchor = W, side="right")

        P2 = Radiobutton(root, text="Kelompok 5 huruf", value=1, command = lambda : self.getOutputType(P2))
        P2.pack( anchor = W, side="right")


        # Field Edit Plaintext
        self.Text_plaintext = Label(self, text = "Enter the plaintext")
        self.Text_plaintext.pack(anchor = W)

        self.Edit_plaintext = Text(self, width=80, height=5, font=("Helvetica", 8 ))
        self.Edit_plaintext.pack(anchor = W)

        # Field Edit Key
        self.Text_key = Label(self, text = "Enter the key")
        self.Text_key.pack(anchor = W)

        self.Edit_key = Text(self, width=25, height=2, font=("Helvetica", 8 ))
        self.Edit_key.pack(anchor = W)

        # Button to reset vigenere square (only for full vigenere)
        self.Reset_Square = Button(self, text = "Reset Vigenere Square (only for full vigenere)", command= lambda : self.resetSquare())
        self.Reset_Square.pack(anchor = W, pady = 5)

        # Field Edit Ciphertext
        self.Text_ciphertext = Label(self, text = "Enter the ciphertext")
        self.Text_ciphertext.pack(anchor = W)

        self.Edit_ciphertext = Text(self, width=80, height=5, font=("Helvetica", 8 ))
        self.Edit_ciphertext.pack(anchor = W)

        # Button to Encrypt
        self.Button_encrypt = Button(self, text = "Encrypt Text", command= lambda : self.runEncrypt())
        self.Button_encrypt.pack(pady = 5, padx = 5, side = "left")

        # Button to Decrypt
        self.Button_decrypt = Button(self, text = "Decrypt Text", command= lambda : self.runDecrypt())
        self.Button_decrypt.pack(pady = 5, padx = 5, side = "left")

        # Button load file
        self.Button_load = Button(self, text = "Load File", command= lambda : self.onOpen())
        self.Button_load.pack(pady = 5, padx = 5, side = "right")

        # Button save file
        self.Button_save = Button(self, text = "Save File", command= lambda : self.writeFile())
        self.Button_save.pack(pady = 5, padx = 5, side = "right")


    def getScript(self, Rb):
        print(Rb["text"])
        self.selected_algorithm = Rb["value"]
        
    def getOutputType(self, Rb):
        print(Rb["text"])
        self.output_type = Rb["value"]
        
    def resetSquare(self):
        rand_full_vigenere_square()

    def runEncrypt(self):
        key = self.Edit_key.get("1.0",'end-1c')
        plaintext = self.Edit_plaintext.get("1.0",'end-1c')

        ciphertext = ""

        if (self.selected_algorithm != 4) :
            K = key.replace(" ", "")
            P = plaintext.replace(" ", "")
        else:
            K = key
            P = plaintext

        if (self.selected_algorithm == 1) :
            ciphertext = vigenere(1, K, P)
        elif (self.selected_algorithm == 2) :
            ciphertext = full_vigenere(1, K, P)
        elif (self.selected_algorithm == 3) :
            ciphertext = auto_key_vigenere(1, K, P)
        elif (self.selected_algorithm == 4) :
            ciphertext = extended_vigenere(1, K, P)
        elif (self.selected_algorithm == 5) :
            pass
        elif (self.selected_algorithm == 6) :
            ciphertext = super_enkripsi(1, K, P)
        elif (self.selected_algorithm == 7) :
            pass
        elif (self.selected_algorithm == 8) :
            pass
        elif (self.selected_algorithm == 9) :
            pass
        else:
            print("Select the algorithm first !!")

        if (ciphertext != ""):
            self.Edit_plaintext.delete('1.0',END)
            self.Edit_ciphertext.delete('1.0',END)
            self.Edit_ciphertext.insert('1.0',ciphertext)

    def runDecrypt(self):
        key = self.Edit_key.get("1.0",'end-1c')
        plaintext = self.Edit_plaintext.get("1.0",'end-1c')

        ciphertext = ""

        if (self.selected_algorithm != 4) :
            K = key.replace(" ", "")
            P = plaintext.replace(" ", "")
        else:
            K = key
            P = plaintext

        if (self.selected_algorithm == 1) :
            ciphertext = vigenere(-1, K, P)
        elif (self.selected_algorithm == 2) :
            ciphertext = full_vigenere(-1, K, P)
        elif (self.selected_algorithm == 3) :
            ciphertext = auto_key_vigenere(-1, K, P)
        elif (self.selected_algorithm == 4) :
            ciphertext = extended_vigenere(-1, K, P)
        elif (self.selected_algorithm == 5) :
            pass
        elif (self.selected_algorithm == 6) :
            ciphertext = super_enkripsi(-1, K, P)
        elif (self.selected_algorithm == 7) :
            pass
        elif (self.selected_algorithm == 8) :
            pass
        elif (self.selected_algorithm == 9) :
            pass
        else:
            print("Select the algorithm first !!")

        if (ciphertext != ""):
            self.Edit_plaintext.delete('1.0',END)
            self.Edit_ciphertext.delete('1.0',END)
            self.Edit_ciphertext.insert('1.0',ciphertext)

    def onOpen(self):
        fl = filedialog.askopenfilename(title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))

        if fl != '':
            text = self.readFile(fl)
            self.filename = fl
            self.Edit_ciphertext.delete('1.0',END)
            self.Edit_plaintext.delete('1.0',END)
            self.Edit_plaintext.insert(END, text)

    def readFile(self, filename):
        self.f = open(filename, "r+")
        text = self.f.read()
        return text

    def writeFile(self):
        self.f = open(self.filename, "w+")
        rewrite = self.f.write(self.Edit_ciphertext.get("1.0",'end-1c'))
        if (rewrite) :
            print("File berhasil disimpan")
        self.f.close()




root = Tk()
app = Application(master=root)
app.master.title("Kriptografi Encrypt Decrypt Application")
app.master.geometry("550x550")
app.mainloop()
root.destroy()