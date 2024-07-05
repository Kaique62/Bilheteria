import tkinter.messagebox
from customtkinter import *
import tkinter
from PIL import ImageTk, Image
import Bilheteria
import json

logins = {}

with open(r'C:\Users\997979\Codigos Python\Aulas Senac\UC5\arquivos adicionais\cadastro.json', 'r') as file:
    try:
        logins = json.load(file)
    except:
        print("Sem cadastros para carregar!")
        
def confirmar(usuario, senha, app):
    try:
        if usuario in logins and senha == logins[usuario]:
            tkinter.messagebox.showinfo('Logado com Sucesso',f"Bem Vindo!\n{usuario}")
            Bilheteria.start(app, usuario)
        else:
            tkinter.messagebox.showerror('Login Inválido',"Usuário ou senha incorretos!") 
    except:
        tkinter.messagebox.showerror('Login Inválido',"Usuário ou senha incorretos!")

def realizarCadastro(usuario, senha, senhaConfirm, app):
    global logins
    if usuario not in logins and senha == senhaConfirm:
        tkinter.messagebox.showinfo('Cadastro Realizado com Sucesso', "Usuário Cadastrado!")
        logins[usuario] = senha
        with open('arquivos adicionais/cadastro.json', 'w') as file:
            json.dump(logins, file)
        print(logins)
        startup(app)
        
    elif usuario in logins:
        tkinter.messagebox.showerror('Cadastro Inválido',"Usuário já cadastrado ")
    else:
        tkinter.messagebox.showerror('Cadastro Inválido',"Senhas não se coincidem ")

def telaDeCadastro(app):    
    print(logins)
    for i in app.winfo_children():
        i.destroy()
    
    labelUser = CTkLabel(app, text="Usuário")
    labelUser.pack(padx=0, pady=5)

    usuario = CTkEntry(app)
    usuario.pack(pady=5)

    labelsenha = CTkLabel(app, text="Senha")
    labelsenha.pack(padx=0, pady=5)
    
    senha = CTkEntry(app, show="*")
    senha.pack(padx=0, pady=5)
    
    confirmarSenhaLabel = CTkLabel(app, text="Confirme sua Senha")
    confirmarSenhaLabel.pack(padx=0, pady=5)
    
    senhaConfirm = CTkEntry(app, show="*")
    senhaConfirm.pack(padx=0, pady=5)
    
    login = CTkButton(app, text="Cadastrar-se", command=lambda: realizarCadastro(usuario.get(), senha.get(), senhaConfirm.get(), app))
    login.pack(padx=10, pady=10)
    
    cancelar = CTkButton(app, text="Sair", command=lambda: startup(app))
    cancelar.pack(pady=10, padx=10)

def startup(app):

    for i in app.winfo_children():
        i.destroy()

    image = ImageTk.PhotoImage(Image.open(r'arquivos adicionais\200w.gif').resize((100, 100)))
    CTkLabel(app, image=image, text='').pack()

    labelUser = CTkLabel(app, text="Usuário")
    labelUser.pack(padx=0, pady=5)

    usuario = CTkEntry(app)
    usuario.pack(pady=5)

    labelsenha = CTkLabel(app, text="Senha")
    labelsenha.pack(padx=0, pady=5)

    senha = CTkEntry(app, show="*")
    senha.pack(padx=0, pady=5)

    login = CTkButton(app, text="Login", command=lambda: confirmar(usuario.get(), senha.get(), app))
    login.pack(padx=10, pady=10)

    cancelar = CTkButton(app, text="Sair", command=lambda: exit(0))
    cancelar.pack(pady=10, padx=10)

    cadastrarLabel = CTkLabel(app, text='Cadastrar se')
    cadastrarLabel.pack()
    cadastrarLabel.bind("<Button-1>", lambda e:
        telaDeCadastro(app))