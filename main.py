from tkinter import *
from vigenere import *


# selected_algoritm = 0

class Application(Frame):
    selected_algoritm = 0

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # RadioButton
        var = IntVar()

        R1 = Radiobutton(root, text="Standard Vigenere Cipher", variable=var, value=1, command = lambda : self.getScript(R1))
        R1.pack( anchor = W )

        R2 = Radiobutton(root, text="Full Vigenere Cipher", variable=var, value=2, command = lambda : self.getScript(R2))
        R2.pack( anchor = W )

        R3 = Radiobutton(root, text="Auto-key Vigenere Cipher", variable=var, value=3, command = lambda : self.getScript(R3))
        R3.pack( anchor = W)

        R4 = Radiobutton(root, text="Expanded Vigenere Cipher", variable=var, value=4, command = lambda : self.getScript(R4))
        R4.pack( anchor = W )

        R5 = Radiobutton(root, text="Playfair Cipher", variable=var, value=5, command = lambda : self.getScript(R5))
        R5.pack( anchor = W )

        R6 = Radiobutton(root, text="Super Enkripsi", variable=var, value=6, command = lambda : self.getScript(R6))
        R6.pack( anchor = W)

        R7 = Radiobutton(root, text="Affine Cipher", variable=var, value=7, command = lambda : self.getScript(R7))
        R7.pack( anchor = W )

        R8 = Radiobutton(root, text="Hill Cipher", variable=var, value=8, command = lambda : self.getScript(R8))
        R8.pack( anchor = W )

        R9 = Radiobutton(root, text="Enigma Cipher", variable=var, value=9, command = lambda : self.getScript(R9))
        R9.pack( anchor = W)


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


    def getScript(self, Rb):
        print(Rb["text"])
        self.selected_algoritm = Rb["value"]
        

    def runEncrypt(self):
        key = self.Edit_key.get("1.0",'end-1c')
        plaintext = self.Edit_plaintext.get("1.0",'end-1c')

        ciphertext = ""

        if (self.selected_algoritm != 4) :
            K = key.replace(" ", "")
            P = plaintext.replace(" ", "")

        if (self.selected_algoritm == 1) :
            ciphertext = vigenere(1, K, P)
        elif (self.selected_algoritm == 2) :
            pass
        elif (self.selected_algoritm == 3) :
            ciphertext = auto_key_vigenere(1, K, P)
        elif (self.selected_algoritm == 4) :
            ciphertext = extended_vigenere(1, K, P)
        elif (self.selected_algoritm == 5) :
            pass
        elif (self.selected_algoritm == 6) :
            ciphertext = super_enkripsi(1, K, P)
        elif (self.selected_algoritm == 7) :
            pass
        elif (self.selected_algoritm == 8) :
            pass
        elif (self.selected_algoritm == 9) :
            pass
        else:
            print("Select the algorithm first !!")

        if (ciphertext != ""):
            self.Edit_plaintext.delete('1.0',END)
            self.Edit_ciphertext.delete('1.0',END)
            self.Edit_ciphertext.insert('1.0',ciphertext)

    def runDecrypt(self):
        key = self.Edit_key.get("1.0",'end-1c')
        ciphertext = self.Edit_ciphertext.get("1.0",'end-1c')

        plaintext = ""

        if (self.selected_algoritm != 4) :
            K = key.replace(" ", "")
            P = ciphertext.replace(" ", "")

        if (self.selected_algoritm == 1) :
            plaintext = vigenere(-1, K, P)
        elif (self.selected_algoritm == 2) :
            pass
        elif (self.selected_algoritm == 3) :
            plaintext = auto_key_vigenere(-1, K, P)
        elif (self.selected_algoritm == 4) :
            plaintext = extended_vigenere(-1, K, P)
        elif (self.selected_algoritm == 5) :
            pass
        elif (self.selected_algoritm == 6) :
            plaintext = super_enkripsi(-1, K, P)
        elif (self.selected_algoritm == 7) :
            pass
        elif (self.selected_algoritm == 8) :
            pass
        elif (self.selected_algoritm == 9) :
            pass
        else:
            print("Select the algorithm first !!")

        if (plaintext != ""):
            self.Edit_ciphertext.delete('1.0',END)
            self.Edit_plaintext.delete('1.0',END)
            self.Edit_plaintext.insert('1.0',plaintext)



root = Tk()
app = Application(master=root)
app.master.title("Kriptografi Encrypt Decrypt Application")
app.master.geometry("500x500")
app.mainloop()
root.destroy()