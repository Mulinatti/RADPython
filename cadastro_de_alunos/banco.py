import sqlite3
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

conexao = sqlite3.connect("database.db")

cursor = conexao.cursor()

def iniciar_banco():

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_curso TEXT NOT NULL
        );
        '''
    )

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aluno (
            id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            curso_id INTEGER,
            email TEXT UNIQUE NOT NULL,
            FOREIGN KEY (curso_id) REFERENCES cursos(id_curso)
        );
    '''
    )

    conexao.commit()

def cadastrar_curso(nome_curso):
    cursor.execute(f'INSERT INTO cursos(nome_curso) VALUES ("{nome_curso}")')
    conexao.commit()

def cadastrar_aluno(nome, email, curso):
    print(nome, email, curso)

def busca_aluno(termo_de_busca):
    cursor.execute(f'SELECT * FROM aluno WHERE nome LIKE "{termo_de_busca}%" OR id_aluno = "{termo_de_busca}" OR curso_id IN (SELECT id_curso FROM cursos WHERE nome_curso LIKE "{termo_de_busca}%")')
    alunos = cursor.fetchall()

    if len(alunos) == 0:
        print(Fore.BLUE + "\nNenhum aluno encontrado com esse termo de busca" + Style.RESET_ALL)
        return
    
    printar_aluno(alunos)

def listar_alunos():
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    printar_aluno(alunos)

def verificar_curso(curso_pretendido):
    cursor.execute("SELECT * FROM cursos")
    cursos = cursor.fetchall()

    if len(cursos) < 1:
        print(Fore.RED + "\nNão existem cursos cadastrados!" + Style.RESET_ALL)

    for curso in cursos:
        if curso[0] == curso_pretendido:
            return curso[1]

        if curso[1] == curso_pretendido:
            return curso[0]
    
    return False


def printar_aluno(alunos):
    for aluno in alunos:
        print(f'{Fore.CYAN}ID:{Style.RESET_ALL} {aluno[0]} | {Fore.CYAN}Nome:{Style.RESET_ALL} {aluno[1]} | {Fore.CYAN}Curso:{Style.RESET_ALL} {verificar_curso(aluno[2])} | {Fore.CYAN}E-Mail:{Style.RESET_ALL} {aluno[3]}\n')


def fechar_banco():
    conexao.close()
