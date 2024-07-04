from customtkinter import *
from tkinter.messagebox import *
import json
import os

def path():
    return 'arquivos adicionais/bilhetesData.json'

if not os.path.exists('arquivos adicionais'):
    os.makedirs('arquivos adicionais')

open(path(), 'a+').close()

data = {}

with open(path(), 'r') as file:
    try:
        data = json.load(file)
    except:
        print('First Time Loading')


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

app = CTk()
app.geometry("360x720")

nameLabel =  CTkLabel(app, text="Nome do Portador", justify="center")
nameLabel.pack(pady=3, anchor='w')

nome = CTkEntry(app)
nome.pack(anchor='w', pady=3)

ingressoLabel = CTkLabel(app, text="Tipo de Ingresso")
ingressoLabel.pack(anchor='w')

opt = IntVar()

button1 = CTkRadioButton(app, text="Pista", variable=opt, value=1)
button1.pack(anchor='w')

opt.set(1)

button2 = CTkRadioButton(app, text="Camarote", variable=opt)
button2.pack(anchor='w')

necessityLabel =  CTkLabel(app, text="Necessidades Especiais")
necessityLabel.pack(anchor='w')

var1 = BooleanVar()
box1 = CTkCheckBox(app, text="Rampa de Acesso", variable=var1)
box1.pack(anchor='w')

var2 = BooleanVar()
box2 = CTkCheckBox(app, text="Intérprete", variable=var2)
box2.pack(anchor='w')

var3 = BooleanVar()
box3 = CTkCheckBox(app, text="Sala Sensorial", variable=var3)
box3.pack(anchor='w')

confirm = CTkButton(app, text="Enviar", command=saveData)
confirm.pack(anchor='w')

app.mainloop()