import time
import os
from colorama import Fore, Back, Style, init
from banco import *

init(autoreset=True)

nome_arquivo = "cadastro_de_alunos/alunos.txt"

def mostrar_opcoes():
    print(Fore.YELLOW + "ESCOLHA UMA DAS OPÇÕES\n" + Style.RESET_ALL)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Cadastrar curso")
    print("5 - Sair")


def cadastrar():
    print(Fore.YELLOW + "Informe os dados para cadastrar o aluno\n" + Style.RESET_ALL)

    nome = input("Informe o nome do aluno: ").split()
    curso = input("Informe o curso do aluno: ").split()
    email = input("Informe o E-Mail do aluno: ").split()

    nome = " ".join(nome)
    curso = " ".join(curso)
    email = " ".join(email)

    if len(nome) == 0 or len(curso) == 0 or len(email) == 0:
        os.system("cls")
        print(Fore.RED + "\nPreencha todos os campos." + Style.RESET_ALL)
        time.sleep(3)
        return

    for caractere in nome:
        if caractere.isdigit():
            print(Fore.RED + "\nO Campo NOME não pode possuir números." + Style.RESET_ALL)
            print(Fore.BLUE + "\nO Cadastro não foi efetuado." + Style.RESET_ALL)
            time.sleep(3)
            return
        
    for caractere in curso:
        if caractere.isdigit():
            print(Fore.RED + "\nO Campo CURSO não pode possuir números." + Style.RESET_ALL)
            print(Fore.BLUE + "\nO Cadastro não foi efetuado." + Style.RESET_ALL)
            time.sleep(3)
            return
        
    cadastrar_aluno(nome, email, curso)
    


def mostrar_alunos():
    listar_alunos()
    continuar = input(Fore.BLUE + "\nPressione ENTER para continuar..." + Style.RESET_ALL)


def buscar_aluno():
    termo_de_busca = input(Fore.YELLOW + "Informe o termo de busca: " + Style.RESET_ALL)

    busca_aluno(termo_de_busca)
    continuar = input(Fore.BLUE + "\nPressione ENTER para continuar..." + Style.RESET_ALL)


def cadastro_curso():
    print(Fore.YELLOW + "CADASTRO DE CURSO\n" + Style.RESET_ALL)

    nome_curso = input("Digite o nome do curso a ser criado: ").split()

    nome_curso = " ".join(nome_curso)

    if len(nome_curso) == 0:
        print(Fore.RED + "\nO nome do curso não pode estar vazio!" + Style.RESET_ALL)
        time.sleep(3)
        return
    
    for caractere in nome_curso:
        if caractere.isdigit():
            print(Fore.RED + "\nO nome do curso não pode conter números!" + Style.RESET_ALL)
            time.sleep(3)
            return
    
    cadastrar_curso(nome_curso)