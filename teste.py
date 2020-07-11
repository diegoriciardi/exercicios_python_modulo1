#!/usr/bin/python3

#try:
#    nome = int(input("Digite seu nome: "))
#    print(nome)
#except ValueError as e:
#    print("Mano....presta atencao no bagulho, precisa digitar numero")

#ling = input("digite a melhor linguagem de programação: ")
#
#if ling.lower().strip() == 'python':
#    print("você acertou")
#else:
#    print("Você errou")


numero = input("Digite um numero: ")

try:
    if numero.isnumeric():
        print(int(numero) + 2)
except Exception:
    print("{} não é um número!".format(numero))
