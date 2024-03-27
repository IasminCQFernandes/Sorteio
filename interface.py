import tkinter as tk
from tkinter import messagebox
import random

# Variáveis globais
participantes = ['ana', 'vitoria', 'victor', 'pedro']
participantes_sorteados = []
nome_sorteio = 'Grupo'

# Função para adicionar participante
def add_participante():
    nome = entrada_nome.get()
    if nome:
        participantes.append(nome)
        lista_participantes.insert(tk.END, nome)
        entrada_nome.delete(0, tk.END)
        messagebox.showinfo("Sucesso", f'O nome "{nome}" foi adicionado à lista de participantes do grupo {nome_sorteio}!')
    else:
        messagebox.showwarning("Atenção", "Por favor, insira um nome.")

# Função para realizar o sorteio
def sorteio():
    nome_sorteado = random.choice(participantes)
    return nome_sorteado

def realizar_sorteio():
    participante = entrada_participante.get()
    if participante not in participantes:
        messagebox.showwarning("Atenção", "Você não está na lista de participantes.")
        return
    
    sorteado = sorteio()
    while sorteado == participante:
        sorteado = sorteio()
    
    participantes_sorteados.append(sorteado)
    participantes.remove(sorteado)
    messagebox.showinfo("Sorteio realizado", f'O amigo oculto de {participante} é: {sorteado}!')
    lista_participantes_sorteados.insert(tk.END, sorteado)
    lista_participantes.delete(participantes.index(sorteado))

# Configuração da interface
root = tk.Tk()
root.title("Sorteio de Amigo Oculto")

# Frames
frame_adicionar = tk.Frame(root)
frame_adicionar.pack(pady=10)

frame_sorteio = tk.Frame(root)
frame_sorteio.pack(pady=10)

# Entrada de nome
label_nome = tk.Label(frame_adicionar, text="Digite um participante:")
label_nome.grid(row=0, column=0)

entrada_nome = tk.Entry(frame_adicionar, width=30)
entrada_nome.grid(row=0, column=1)

botao_adicionar = tk.Button(frame_adicionar, text="Adicionar", command=add_participante)
botao_adicionar.grid(row=0, column=2, padx=10)

# Lista de participantes
lista_participantes = tk.Listbox(frame_adicionar, width=40)
lista_participantes.grid(row=1, column=0, columnspan=3, padx=10)

for participante in participantes:
    lista_participantes.insert(tk.END, participante)

# Entrada de nome para sorteio
label_participante = tk.Label(frame_sorteio, text="Qual o seu nome:")
label_participante.grid(row=0, column=0)

entrada_participante = tk.Entry(frame_sorteio, width=30)
entrada_participante.grid(row=0, column=1)

botao_sorteio = tk.Button(frame_sorteio, text="Realizar Sorteio", command=realizar_sorteio)
botao_sorteio.grid(row=0, column=2, padx=10)

# Lista de participantes sorteados
lista_participantes_sorteados = tk.Listbox(frame_sorteio, width=40)
lista_participantes_sorteados.grid(row=1, column=0, columnspan=3, padx=10)

# Iniciar GUI
root.mainloop()
