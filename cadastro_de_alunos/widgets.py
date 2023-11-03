import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk

def widget_input_nome(frame):
    nome_label = ttk.Label(frame, text="Nome:")
    nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    nome_entry = ttk.Entry(frame, width=40)  
    nome_entry.grid(row=0, column=1, padx=5, pady=5)


def widget_input_email(frame):
    email_label = ttk.Label(frame, text="E-Mail:")
    email_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    email_entry = ttk.Entry(frame, width=40)  
    email_entry.grid(row=1, column=1, padx=5, pady=5)


def widget_input_curso(frame):
    curso_label = ttk.Label(frame, text="Curso:")
    curso_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    curso_entry = ttk.Entry(frame, width=40)  
    curso_entry.grid(row=2, column=1, padx=5, pady=5)

    
def widget_cadastrar_button(frame):
    cadastrar_button = ttk.Button(frame, text="Cadastrar", style="TButton")
    cadastrar_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")




def widget_cadastro_curso(frame):
    frame_cadastrar_curso = ttk.Frame(frame)
    frame_cadastrar_curso.grid(row=4, column=0, columnspan=3, pady=5, sticky="w")

    curso_cadastrar_label = ttk.Label(frame_cadastrar_curso, text="Cadastrar Curso:")
    curso_cadastrar_label.grid(row=0, column=0, padx=(15, 15), pady=5, sticky="w")
    curso_cadastrar_entry = ttk.Entry(frame_cadastrar_curso, width=40)  # Ajuste o tamanho conforme necessário
    curso_cadastrar_entry.grid(row=1, column=0, padx=(15, 15), pady=5, sticky="w")

    cadastrar_curso_button = ttk.Button(frame_cadastrar_curso, text="Cadastrar Curso", style="Blue.TButton")
    cadastrar_curso_button.grid(row=2, column=0, padx=(15, 15), pady=5, sticky="w")


def widget_buscar_aluno(frame):
    buscar_label = ttk.Label(frame, text="Buscar Aluno:")
    buscar_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
    buscar_entry = ttk.Entry(frame, width=40)
    buscar_entry.grid(row=6, column=1, padx=5, pady=5)
    buscar_button = ttk.Button(frame, text="Buscar Aluno", style="Blue.TButton")
    buscar_button.grid(row=6, column=2, padx=5, pady=5, sticky="w")


def widget_listar_alunos(frame):
    alunos_cadastrados_label = ttk.Label(frame, text="Alunos Cadastrados:")
    alunos_cadastrados_label.grid(row=7, columnspan=3, pady=5, sticky="n")
    alunos_cadastrados = tk.Text(frame, wrap="none", state="disabled", height=10, width=80)
    alunos_cadastrados.grid(row=8, columnspan=3, pady=10)