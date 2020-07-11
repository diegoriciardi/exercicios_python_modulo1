#!/usr/bin/python3

#try:
#    numero = int("2")
#    print(numero)
#    dicionario = { 'nome': 'Paulo', 'nome': 'Italo' }
#    print(dicionario['nome'])
#    print(5 / 0)
#except ValueError as e:
#    print(e)
#except ZeroDivisionError as e:
#    print(e)
#except KeyError as e:
#    print(e)

#produtos = [
#            {'nome': 'caneta', 'valor': 2.0 },
#            {'nome': 'borracha', 'valor': 1.0 },
#            {'nome': 'lápis', 'valor': 2.5 },
#            {'nome': 'mochila', 'valor': float('3.0') }
#       ]

#try:
#    for produto in produtos:
#        produto['valor'] += produto['valor'] * 0.1
#        print(produto)
#except Exception as e:
#    print(e)
   # pass
#finally:
    #print(produtos)






# aula 4.3 criar excecoes
# Raise exception

# sintaxe

#try:
#   comandos
#   raise Except_Type
#except Except_Type
#    print(e)

#linguagem = input("qual a melhor linguagem de programação? ")
#
#try:
#    if linguagem.lower().strip() == 'python':
#        print("Você acertou")
#    else:
#        raise ValueError('Linguagem errada')
#except ValueError as e:
#    print("ERRO {}".format(e))

# Aula 4.4 manipular arquivos

#arquivo = open('frutas.txt', 'a')

#arquivo.write('melancia\n')

#arquivo.close()

#with open('frutas.txt', 'w') as f:
#    f.write('limao\n')
#    f.write('melancia\n')

dicionario = {}
with open('arquivo.txt', 'r') as f:
    #chave = f.readlines()
    lista = f.read().split("\n")
    for registro in lista:
        if registro != "":
            novaLista = registro.split(" ")
            chave, valor = novaLista[0], novaLista[1]
            dicionario[chave] = valor
    #chave, valor = lista[0].split()

print(dicionario)


try
    print("mano")
except Exception:
    print("erro")
