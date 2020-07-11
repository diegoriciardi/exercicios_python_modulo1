#!/usr/bin/python3
try:
    with open('desafio_manipulacao_arquivos.txt', 'r') as f:
        conteudo = [x for x in f if x != '\n']
        for x in range(len(conteudo)):
            conteudo[x] = "{} - {}".format(x+1, conteudo[x])
        print(conteudo)

    with open('desafio_manipulacao_arquivos.txt', 'w') as f:
        f.writelines(conteudo)
except FileNotFoundError:
    print("O arquivo não existe")
except Exception as e:
    print("Erro: {}".format(e))
