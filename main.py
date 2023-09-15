import tkinter as tk
from tkinter import ttk
from methods import productos_medios
from tkinter import messagebox

# Crea Tabla 
def create_table(root, fields, data):
    # Crear el árbol (Treeview)
    tree = ttk.Treeview(root, columns=fields, show="headings")
    # Definir configuraciones de estilo
    tree.tag_configure("oddrow", background="lightblue")
    tree.tag_configure("evenrow", background="white", foreground="blue")
    # Configurar las columnas
    for field in fields:
        tree.heading(field, text=field)
        tree.column(field, width=100)
    
    # Insertar los datos en la tabla
    for row in data:
        tree.insert("", "end", values=row)
    
    # Mostrar la tabla
    tree.grid(row=50,column=0,columnspan=5,pady=40)


fields = ["n","x0","x00","x0*x00","largo","centro","ri"]
data = [
            (0,0,0,0,0,0,0)
        ]
# FUNCIONES DE LA GUI

def mostrar_error():
    messagebox.showerror("Error", "¡Ocurrió un error!")
    
def show_table():
    if ent_num1.get().isalpha() or ent_num2.get().isalpha() or ent_num3.get().isalpha():
        mostrar_error()
        return
    sem1 = int(ent_num1.get())
    sem2 = int(ent_num2.get())
    iteraciones = int(ent_num3.get())
    data = productos_medios(sem1,sem2,iteraciones)
    create_table(root,fields,data)


root = tk.Tk()

root.geometry("800x600")
lbl_num1=tk.Label(root, text="Semilla1: ")
ent_num1=tk.Entry(root)

lbl_num2=tk.Label(root, text="Semilla2: ")
ent_num2=tk.Entry(root)

lbl_num3=tk.Label(root, text="Iteraciones: ")
ent_num3=tk.Entry(root)

btn_active = tk.Button(root,text="Calcular",command=show_table)


lbl_num1.grid(row=0,column=0,padx=10)
ent_num1.grid(row=0,column=1,padx=10)
lbl_num2.grid(row=1,column=0,padx=10)
ent_num2.grid(row=1,column=1,padx=10)
lbl_num3.grid(row=2,column=0,padx=10)
ent_num3.grid(row=2,column=1,padx=10)
btn_active.grid(row=3,column=0,padx=30, pady=10)

root.mainloop()