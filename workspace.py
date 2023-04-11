from os import path
import csv

BASE_DIR_IN = path.join(path.dirname(__file__),"in")
BASE_DIR_OUT = path.join(path.dirname(__file__), "out")

def criarEntrada():

    '''Cria o arquivo e fornece as entradas'''

    filename = path.join(BASE_DIR_IN, "registro.txt")

    with open(filename, "a") as file:

        separator = ";"
        nome_aluno = input("Nome do aluno: ")
        matricula = input("Matricula: ")
        disciplina = input("Disciplina: ")
        notas = input("Notas AV1, AV2 e AV3: ")

        newlist = [nome_aluno, matricula, disciplina, notas]

        lines = separator.join(newlist)
        file.write(lines)
        file.write("\n")

def saida1():
    
    '''Lê o arquivo txt, identifica os registros separadamente, e escreve em csv por disciplina'''

    filename = path.join(BASE_DIR_IN, "registro.txt")

    with open (filename, "r") as file:

        for lines in file:
            line = lines.split(";")
            nome_aluno = line[0]
            matricula = line[1]
            disciplina = line[2]

            filecsv = path.join(BASE_DIR_OUT, f"{disciplina}.csv")

            with open(filecsv, "a") as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=";")
                csvwriter.writerow([nome_aluno, matricula])

def saida2():

    '''Lê o arquivo txt, identifica os registros separadamente, separa as notas, calcula a situação e escreve em csv por disciplina'''

    filename = path.join(BASE_DIR_IN, "registro.txt")

    with open(filename, "r") as file:

        for lines in file:
            line = lines.split(";")
            matricula = line[1]
            disciplina = line[2]
            av = line[3].strip("\n").strip()

            av1 = int(av[0:2])
            av2 = int(av[3:5])
            av3 = int(av[6:8])

            media = (av1 + av2 + av3) / 3

            if media >= 600:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"

            filecsv = path.join(BASE_DIR_OUT, f"{disciplina}_notas.csv")

            with open(filecsv,"a") as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=";")
                csvwriter.writerow([matricula,av1,av2,av3,situacao])
                


