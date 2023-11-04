import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
from banco import *

def cadastrar_button_click():
    nome = nome_entry.get()
    email = email_entry.get()
    curso = curso_entry.get()

    if not nome or not email or not curso:
        messagebox.showwarning("Aviso", "PREENCHA TODOS OS CAMPOS")
        return

    if cadastrar_aluno(nome, email, curso):
        messagebox.showinfo("Sucesso", "Aluno Cadastrado!")

    else:
        messagebox.showwarning("Error", "Curso não existe")
def listar_alunos_cadastrados():
    alunos = listar_alunos()
    
    if alunos is not None:
        alunos_cadastrados.config(state="normal")
        alunos_cadastrados.delete(1.0, tk.END)

        for aluno in alunos:
            alunos_cadastrados.insert(tk.END, f"ID: {aluno[0]}Nome: {aluno[1]}Curso: {verificar_curso(aluno[2])}")
            alunos_cadastrados.insert(tk.END)

        alunos_cadastrados.config(state="disabled")
        


def cadastrar_curso_button_click():
    nome_curso = curso_cadastrar_entry.get()

    if len(nome_curso) != 0:
        cadastrar_curso(nome_curso)
        messagebox.showinfo("Sucesso", "Curso cadastrado!")
    else:
        messagebox.showwarning("Aviso", "Preencha o campo!")
        return


def buscar_aluno_click():
    termo = buscar_entry.get()
    alunos_encontrados = busca_aluno(termo)

    alunos_cadastrados.config(state="normal")
    alunos_cadastrados.delete(1.0, tk.END)

    if alunos_encontrados:
        aluno = alunos_encontrados[0]  
        id_aluno = aluno[0]
        nome_aluno = aluno[1]
        curso_aluno = verificar_curso(aluno[2])
        email_aluno = aluno[3]

        alunos_cadastrados.insert(tk.END, f"ID: {id_aluno}| Nome: {nome_aluno}| Curso: {curso_aluno}| E-Mail: {email_aluno}")
   
        excluir_button["command"] = lambda: excluir_aluno(id_aluno)
    else:
        alunos_cadastrados.insert(tk.END, "Nenhum aluno encontrado")

    alunos_cadastrados.config(state="disabled")

def toggle_theme_arc():
    app.set_theme("arc")
def excluir_aluno(id_aluno):
    confirmacao = messagebox.askyesno("Confirmar remoção", f" deseja excluir o aluno com id {id_aluno}?")

    if confirmacao:
       
        excluir_aluno_banco(id_aluno)
        
        
        listar_alunos_cadastrados()

def toggle_theme_equilux():
    app.set_theme("equilux")


def listar_alunos_cadastrados():
    alunos = listar_alunos()
    
    if alunos is not None:
        alunos_cadastrados.config(state="normal")
        alunos_cadastrados.delete(1.0, tk.END)

        for aluno in alunos:
            aluno_text = f"ID: {aluno[0]} | Nome: {aluno[1]} | Curso: {verificar_curso(aluno[2])}\n"
            alunos_cadastrados.insert(tk.END, aluno_text)

        alunos_cadastrados.config(state="disabled")
    else:
        print("Erro ao listar alunos") 

    
app = ThemedTk(theme="arc")
app.title("Cadastro de Alunos")
app.minsize(600, 400)
app.resizable(False, False)
frame = ttk.Frame(app)
frame.pack()

iniciar_banco()

nome_label = ttk.Label(frame, text="Nome:")
nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
nome_entry = ttk.Entry(frame, width=40)  
nome_entry.grid(row=0, column=1, padx=5, pady=5)
cadastrar_button = ttk.Button(frame, text="Cadastrar", command=cadastrar_button_click, style="TButton")
cadastrar_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")

email_label = ttk.Label(frame, text="E-Mail:")
email_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
email_entry = ttk.Entry(frame, width=40)  
email_entry.grid(row=1, column=1, padx=5, pady=5)

curso_label = ttk.Label(frame, text="Curso:")
curso_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
curso_entry = ttk.Entry(frame, width=40)  
curso_entry.grid(row=2, column=1, padx=5, pady=5)

# linha separa
separator1 = ttk.Separator(frame, orient="horizontal")
separator1.grid(row=3, columnspan=3, sticky="ew", pady=5)
frame_cadastrar_curso = ttk.Frame(frame)
frame_cadastrar_curso.grid(row=4, column=0, columnspan=3, pady=5, sticky="w")
curso_cadastrar_label = ttk.Label(frame_cadastrar_curso, text="Cadastrar Curso:")
curso_cadastrar_label.grid(row=0, column=0, padx=(15, 15), pady=5, sticky="w")
curso_cadastrar_entry = ttk.Entry(frame_cadastrar_curso, width=40) 
curso_cadastrar_entry.grid(row=1, column=0, padx=(15, 15), pady=5, sticky="w")
cadastrar_curso_button = ttk.Button(frame_cadastrar_curso, text="Cadastrar Curso", command=cadastrar_curso_button_click, style="Blue.TButton")
cadastrar_curso_button.grid(row=2, column=0, padx=(15, 15), pady=5, sticky="w")
#linha do meio
separator_vertical = ttk.Frame(frame, style="TSeparator.Vertical.TSeparator")
separator_vertical.grid(row=4, column=1, rowspan=1, sticky="ns", padx=5)
style = ttk.Style()
style.configure("TSeparator.Vertical.TSeparator", background="gray", width=1)
separator2 = ttk.Separator(frame, orient="horizontal")
separator2.grid(row=5, columnspan=3, sticky="ew", pady=5)

# campo Buscar aluno
buscar_label = ttk.Label(frame, text="Buscar Aluno:")
buscar_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
buscar_entry = ttk.Entry(frame, width=40)
buscar_entry.grid(row=6, column=1, padx=5, pady=5)
buscar_button = ttk.Button(frame, text="Buscar Aluno", command=buscar_aluno_click, style="Blue.TButton")
buscar_button.grid(row=6, column=2, padx=5, pady=5, sticky="w")

alunos_cadastrados_label = ttk.Label(frame)
alunos_cadastrados_label.grid(row=7, columnspan=5)

# alunos cadastrados
alunos_cadastrados_label = ttk.Label(frame, text="Alunos Cadastrados:")
alunos_cadastrados_label.grid(row=7, columnspan=3, pady=5, sticky="n")
alunos_cadastrados = tk.Text(frame, wrap="none", state="disabled", height=10, width=80)
alunos_cadastrados.grid(row=8, columnspan=3, pady=10)

listar_alunos_cadastrados()

x = (app.winfo_screenwidth() - app.winfo_reqwidth()) // 2
y = (app.winfo_screenheight() - app.winfo_reqheight()) // 2
app.geometry("+{}+{}".format(x , y))

excluir_button = ttk.Button(frame, text="Excluir aluno", style="Blue.TButton")
excluir_button.grid(row=12, column=0, columnspan=3, pady=9, sticky="n") 

app.mainloop()




