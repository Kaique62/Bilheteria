from customtkinter import *
from tkinter.messagebox import *

def saveData():
    data.append([nome.get(), opt.get(), var1, var2, var3])
    dataPopup()
    
def dataPopup():
    if opt.get() == 1:
        ingresso = 'Pista'
    else:
        ingresso = "Camarote"
        
    if var1.get() == False:
        rampa = "não"
    else:
        rampa = 'sim'
        
    if var2.get() == False:
        interprete = "não"
    else:
        interprete = 'sim'
        
    if var3.get() == False:
        sala = "não"
    else:
        sala = 'sim'
    
    showinfo("Ingresso", f"Nome: {nome.get()}\nTipo de Ingresso: {ingresso}\nRampa de Acesso: {rampa}\nIntérprete: {interprete}\nSala Sensorial: {sala}")

fontPre = ("Helvetica", 20)

app = CTk()
app.geometry("310x460")

data = []

nameLabel =  CTkLabel(app, text="Nome do Portador", justify="center", font=fontPre)
nameLabel.pack(pady=5, anchor='w')

CTk

nome = CTkEntry(app, width=300, font=fontPre)
nome.pack(anchor='w', pady=10)

ingressoLabel = CTkLabel(app, text="Tipo de Ingresso", font=fontPre)
ingressoLabel.pack(anchor='w', pady=10)

opt = IntVar()

button1 = CTkRadioButton(app, text="Pista", variable=opt, value=1, font=fontPre)
button1.pack(anchor='w', pady=5)

opt.set(1)

button2 = CTkRadioButton(app, text="Camarote", variable=opt, font=fontPre)
button2.pack(anchor='w', pady=5)

necessityLabel =  CTkLabel(app, text="Necessidades Especiais", font=fontPre)
necessityLabel.pack(anchor='w', pady=10)

var1 = BooleanVar()
box1 = CTkCheckBox(app, text="Rampa de Acesso", variable=var1, font=fontPre)
box1.pack(anchor='w', pady=4)

var2 = BooleanVar()
box2 = CTkCheckBox(app, text="Intérprete", variable=var2, font=fontPre)
box2.pack(anchor='w', pady=4)

var3 = BooleanVar()
box3 = CTkCheckBox(app, text="Sala Sensorial", variable=var3, font=fontPre)
box3.pack(anchor='w', pady=4)

confirm = CTkButton(app, text="Enviar", command=saveData, font=fontPre)
confirm.pack(anchor='w', pady=15)

app.mainloop()