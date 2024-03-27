import random

participantes = ['ana', 'vitoria', 'victor', 'pedro']

participantes_sorteados = []

nome_sorteio = input('Escolha do grupo: ')

def add_participante():
    nome = input('Digite um participante: ')
    participantes.append(nome)
    print(f'O nome "{nome}" foi adicionado a lista de participantes do grupo {nome_sorteio}!')
    print(participantes)
    return participantes

def sorteio():
    nome_sorteado = random.choice(participantes)
    return nome_sorteado

# print(sorteio())
   
def sorteios(nome):
    participante = input('Qual o seu nome: ')
    if participante not in participantes:
        print('Você não está na lista de participantes.')
        return
    
    sorteado = sorteio()
    while sorteado == nome:
        print('Sorteando novamente!')
        sorteado = sorteio()
    
    participantes_sorteados.append(sorteado)
    participantes.remove(sorteado)
    print(f'O amigo oculto de {nome} é: {sorteado}!')
    print(participantes)
    print(participantes_sorteados)

# Exemplo de uso:
# add_participante()
# add_participante()
# add_participante()
sorteios('emily')


