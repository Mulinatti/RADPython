from opcoes import *
import os
import time
from banco import fechar_banco

from colorama import Fore, Back, Style, init

init(autoreset=True)

iniciar_banco()

while True:
    try:
        os.system("cls")
        mostrar_opcoes()
        opcao = int(input(Fore.YELLOW + "\nEscolha uma opção: " + Style.RESET_ALL))
        os.system("cls")

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            mostrar_alunos()
        elif opcao == 3:
            buscar_aluno()
        elif opcao == 4:
            cadastro_curso()
        elif opcao == 5:
            print(Fore.BLUE + "Encerrando programa" + Style.RESET_ALL)
            fechar_banco()
            break
        else:
            print(Fore.RED + "Digite uma opção válida" + Style.RESET_ALL)
            time.sleep(2)
    except ValueError:
        os.system("cls")
        print(Fore.RED + "Digite o número das opções" + Style.RESET_ALL)
        time.sleep(3)

