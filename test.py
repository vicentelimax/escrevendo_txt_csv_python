import csv
from os import path

dir_in = path.join(path.dirname(__file__),'in')

filename = path.join(dir_in, 'registro.txt')

def sepNotas(notas):

    av1 = int(notas[0:3])
    av2 = int(notas[3:6])
    av3 = int(notas[6:9])

    media = (av1 + av2 + av3) / 3

    if media >= 600:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    return [av1, av2, av3, situacao]

with open (filename, "r") as file:

    for lines in file:
        line = lines.split(";")
        # nome_aluno = print(line[0])
        # matricula = print(line[1])
        av = line[3].strip("\n").strip('')
        # av1 = int(av[0:3])
        # av2 = int(av[3:6])
        # av3 = int(av[6:9])
        print(sepNotas(av))

        
        

