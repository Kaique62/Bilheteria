from customtkinter import *
from tkinter.messagebox import *
import tkinter as tk
import json
import os

if not os.path.exists('arquivos adicionais'):
    os.makedirs('arquivos adicionais')

def path():
    return 'arquivos adicionais/bilhetesData.json'

open(path(), 'a+').close()

data = {}

with open(path(), 'r') as file:
    try:
        data = json.load(file)
    except:
        print('First Time Loading')


def checkBoxes():
    if (opt.get() == 1):
        var2.set(False)
        var3.set(False)
        box2.configure(state=DISABLED)
        box3.configure(state=DISABLED)
    else:
        box2.configure(state=NORMAL)
        box3.configure(state=NORMAL)
        
def saveData():
    data[len(data) + 1] = [nome.get(), opt.get(), var1.get(), var2.get(), var3.get()]
    
    with open(path(), 'w') as file:
        json.dump(data, file)
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

fontPre = ("Calibri", 20)
app = CTk()
app.geometry("310x400")
app.title("Bilhete")

set_appearance_mode("light")

nameLabel =  CTkLabel(app, text="Nome do Portador", justify="center", font=fontPre, )
nameLabel.pack(pady=5, anchor='w')

nome = CTkEntry(app, width=360, font=fontPre)
nome.pack(anchor='w', pady=10)

ingressoLabel = CTkLabel(app, text="Tipo de Ingresso", font=fontPre)
ingressoLabel.pack(anchor='w', pady=10)

opt = IntVar()
opt.set(1)

button1 = CTkRadioButton(app, text="Pista", variable=opt, value=1, font=fontPre, command=checkBoxes)
button1.pack(anchor='w', pady=5)

button2 = CTkRadioButton(app, text="Camarote", variable=opt, font=fontPre, command=checkBoxes)
button2.pack(anchor='w', pady=5)

necessityLabel =  CTkLabel(app, text="Necessidades Especiais", font=fontPre)
necessityLabel.pack(anchor='w', pady=10)

var1 = BooleanVar()
box1 = CTkCheckBox(app, text="Rampa de Acesso", variable=var1, font=fontPre)
box1.pack(anchor='w', pady=4)

var2 = BooleanVar()
box2 = CTkCheckBox(app, text="Intérprete", variable=var2, font=fontPre, state=DISABLED)
box2.pack(anchor='w', pady=4)

var3 = BooleanVar()
box3 = CTkCheckBox(app, text="Sala Sensorial", variable=var3, font=fontPre, state=DISABLED)
box3.pack(anchor='w', pady=4)

confirm = CTkButton(app, text="Enviar", command=saveData, font=fontPre, width=360, height=40)
confirm.pack(anchor='w', pady=10)

app.mainloop()