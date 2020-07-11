#!/usr/bin/python3

#matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
matriz = [ [6, 2, 8], [4, 5, 6], [3, 8, 9] ]

lista1 = []
lista2 = []
contador = 0
soma1 = 0
soma2 = 0

for linha in matriz:
    lista1.append(linha[contador])
    contador += 1

contador = 2

for linha in matriz:
    lista2.append(linha[contador])
    contador -= 1

for numero in lista1:
    soma1 += numero

for numero in lista2:
    soma2 += numero

print("Elementos da diagoonal 1  ==> {}".format(lista1))
print("Elementos da diagoonal 2  ==> {}".format(lista2))
print("Soma diagonal 1           ==> {}".format(soma1))
print("Soma diagonal 2           ==> {}".format(soma2))
print("Soma das diagonais        ==> {}".format(soma1 + soma2))
