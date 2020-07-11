#!/usr/bin/python3

entrada = input("Digite por favos as quatro (4) notas do aluno: ")

nota1 = float(entrada.split()[0])
nota2 = float(entrada.split()[1])
nota3 = float(entrada.split()[2])
nota4 = float(entrada.split()[3])

media = (nota1 + nota2 + nota3 + nota4) / 4
print("media = {}".format(media))
status = ""

if media >= 7:
    status = "Aprovado"
elif media > 3:
    status = "Recuperação"
else:
    status = "Reprovado"
print(status)
