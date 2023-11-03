import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
from banco import cadastrar_aluno, listar_alunos, cadastrar_curso, verificar_curso

def cadastrar_button_click():
    nome = nome_entry.get()
    email = email_entry.get()
    curso = curso_entry.get()

    if len(nome) or len(email) or len(curso) <= 0:
        messagebox.showwarning("Aviso", "PREENCHA TODOS OS CAMPOS")

def cadastrar_curso_button_click():
    nome_curso = curso_cadastrar_entry.get()
    if nome_curso:
        cadastrar_curso(nome_curso)

def toggle_theme_arc():
    app.set_theme("arc")
    update_alunos_cadastrados_theme()

def toggle_theme_equilux():
    app.set_theme("equilux")
    update_alunos_cadastrados_theme()

def listar_alunos_cadastrados():
    alunos = listar_alunos()
    alunos_cadastrados.config(state="normal") 
    alunos_cadastrados.delete(1.0, tk.END)  

    for aluno in alunos:
        alunos_cadastrados.insert(tk.END, f"ID: {aluno[0]}\nNome: {aluno[1]}\nCurso: {verificar_curso(aluno[2])}\n")
        alunos_cadastrados.insert(tk.END, "-" * 50 + "\n") 
        
    alunos_cadastrados.config(state="disabled") 
    update_alunos_cadastrados_theme()

def update_alunos_cadastrados_theme():
    theme = app.get_themes()[0]  
    if "equilux" in theme.lower():
        alunos_cadastrados.configure(bg="black", fg="white")
    else:
        
        alunos_cadastrados.configure(bg="SystemButtonFace", fg="SystemWindowText")#tema claro

app = ThemedTk(theme="arc")
app.title("Cadastro de Alunos")
app.minsize(600, 400)
app.resizable(False, False)
frame = ttk.Frame(app)
frame.pack()
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
curso_cadastrar_entry = ttk.Entry(frame_cadastrar_curso, width=40)  # Ajuste o tamanho conforme necessário
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
buscar_button = ttk.Button(frame, text="Buscar Aluno", style="Blue.TButton")
buscar_button.grid(row=6, column=2, padx=5, pady=5, sticky="w")

# alunos cadastrados
alunos_cadastrados_label = ttk.Label(frame, text="Alunos Cadastrados:")
alunos_cadastrados_label.grid(row=7, columnspan=3, pady=5, sticky="n")
alunos_cadastrados = tk.Text(frame, wrap="none", state="disabled", height=10, width=80)
alunos_cadastrados.grid(row=9, columnspan=3, pady=10)
header_text = "ID                                                            NOME                                                              CURSO                                                 EMAIL\n" 
header_label = ttk.Label(frame, text=header_text)
header_label.grid(row=8, columnspan=3, pady=2, sticky="n")

excluir_button = ttk.Button(frame, text="Excluir aluno", style="Blue.TButton")
excluir_button.grid(row=12, column=0, columnspan=3, pady=9, sticky="n") 



    

x = (app.winfo_screenwidth() - app.winfo_reqwidth()) // 2
y = (app.winfo_screenheight() - app.winfo_reqheight()) // 2
app.geometry("+{}+{}".format(x, y))

app.mainloop()




