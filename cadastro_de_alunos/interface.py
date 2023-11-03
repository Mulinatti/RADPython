import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
from banco import cadastrar_aluno, listar_alunos, cadastrar_curso, verificar_curso
from widgets import *

app = ThemedTk(theme="arc")
app.title("Cadastro de Alunos")
app.minsize(600, 400)
frame = ttk.Frame(app)
frame.pack()

#CHAMADA DOS WIDGETS POR FUNÇÃO

widget_input_nome(frame)
widget_input_email(frame)
widget_input_curso(frame)
widget_cadastrar_button(frame)
widget_cadastro_curso(frame)
widget_buscar_aluno(frame)
widget_listar_alunos(frame)

# linha separa
separator1 = ttk.Separator(frame, orient="horizontal")
separator1.grid(row=3, columnspan=3, sticky="ew", pady=5)

#linha do meio
style = ttk.Style()
style.configure("TSeparator.Vertical.TSeparator", background="gray", width=1)
separator2 = ttk.Separator(frame, orient="horizontal")
separator2.grid(row=5, columnspan=3, sticky="ew", pady=5)

# alunos cadastrados

x = (app.winfo_screenwidth() - app.winfo_reqwidth()) // 2
y = (app.winfo_screenheight() - app.winfo_reqheight()) // 2
app.geometry("+{}+{}".format(x, y))

app.mainloop()




