import LoginScreen as login
from customtkinter import *
import os

if not os.path.exists('arquivos adicionais'):
    os.makedirs('arquivos adicionais')
    print('aa')
    
open(r'arquivos adicionais\bilhetesData.json', 'a+').close()
open(r'arquivos adicionais\cadastro.json', 'a+').close()
    
app = CTk()
app.geometry('360x720')

def clearScreen():
    for i in app.winfo_children():
        i.destroy()

login.startup(app)

app.mainloop()