#!/usr/bin/python3

contador = 1

with open('desafio_manipulacao_arquivos.txt', 'r') as f:
    #lista = f.read().split("\n")
    lista = f.readlines()

#lista.pop()

arquivo = open('desafio_manipulacao_arquivos.txt', 'w')

arquivo.seek(0)

for linha in lista:
    arquivo.write(str(contador) + " "  + linha)
    contador += 1

#with open('desafio_manipulacao_arquivos.txt', 'r') as f:
#    print(f.read())
