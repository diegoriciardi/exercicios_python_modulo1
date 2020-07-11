#!/usr/bin/python3

contador = 1
soma = 0
status = ""

while contador <= 4:
    soma += (float(input("Digite por favor a {} nota do aluno: ".format(contador))))
    contador += 1

media = soma / contador

print("media = {:.2f}".format(media))

if media >= 7:
    status = "Aprovado"
elif media > 3:
    status = "Recuperação"
else:
    status = "Reprovado"

print(status)
