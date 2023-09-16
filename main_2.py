import tkinter as tk
from tkinter import ttk,font
from config import config
from tkinter import messagebox
from methods import productos_medios

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.config = config
        self.window.geometry(self.config.size)
        self.window.title(self.config.title)
        self.frame_main = tk.Frame(self.window)
        self.window.resizable(1, 1)
        self.setup_fonts()
        self.set_styles()
    def set_styles(self):
        
        ttk.Style().configure("Treeview", relief="flat",background="#00a7c7",foreground="white",font=('calibri', 11, 'bold'))
        style_btn = ttk.Style()
        style_btn.theme_use('alt')
        style_btn.configure('TButton', background = '#005585', foreground = 'white',borderwidth=1, focusthickness=3, focuscolor='none',font=('calibri', 11, 'bold'),width=20,height=4,anchor=tk.CENTER, padding=6)
        style_btn.map('TButton', background=[('active','#00a7c7')])
    def create_tabs(self):
        """Crea las pestañas de la interfaz
        """
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook()
        
        # Crear el contenido de cada una de las pestañas.
        self.web_label = ttk.Label(self.notebook,
            text="www.recursospython.com")
        self.forum_label = ttk.Label(self.notebook,
            text="foro.recursospython.com")
        
        # Añadirlas al panel con su respectivo texto.
        self.notebook.add(self.web_label, text="Web", padding=20)
        self.notebook.add(self.forum_label, text="Foro", padding=20)
        
        self.notebook.pack(padx=10, pady=10)
    def setup_fonts(self):
        self.font_style = font.Font(weight="bold", family="Arial")
        self.window.option_add("*Font", self.font_style)
    def create_labels(self):
        """Crea los labels de la interfaz"""
        self.lbl_num1=tk.Label(self.frame_main, text="Semilla1: ")
        self.lbl_num2=tk.Label(self.frame_main, text="Semilla2: ")
        self.lbl_num3=tk.Label(self.frame_main, text="Iteraciones: ")
    def create_entries(self):
        """Crea los entries de la interfaz"""
        self.ent_num1=tk.Entry(self.frame_main)
        self.ent_num2=tk.Entry(self.frame_main)
        self.ent_num3=tk.Entry(self.frame_main)
    def create_buttons(self):
        """Crea los botones de la interfaz"""
        self.btn_active = ttk.Button(self.frame_main,text="Calcular",command=self.show_table)
    def create_table(self,window, fields, data):
        """Crea la tabla de la interfaz
        """
        # Crear el árbol (Treeview)
        tree = ttk.Treeview(window, columns=fields, show="headings",height=20)
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.grid(row=50,column=5,sticky="ns",pady=40)
        tree.configure(yscrollcommand=scrollbar.set)
        # Definir configuraciones de estilo
        tree.tag_configure("odd",background="#cdd7ea",foreground="black")
        tree.tag_configure("repeat",background="red",foreground="white")
        
        # Configurar las columnas
        for field in fields:
            tree.heading(field, text=field)
            tree.column(field, width=100)
        # Insertar los datos en la tabla
        for i,row in enumerate(data):
            ttt=list(row[5])
            if i % 2 == 0:
                tree.insert("", "end", values=row,tags=("odd",))
            elif ttt[0]=="-":
                tree.insert("", "end", values=row,tags=("repeat",))
            else: 
                tree.insert("", "end", values=row)
        # Mostrar la tabla
        tree.grid(row=50,column=0,columnspan=5,pady=40,padx=10)
    def management_layout(self):
        """Maneja el diseño de la interfaz
        """
        self.frame_main.grid(row=0,column=0,padx=10,pady=10)
        self.create_tabs()
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.lbl_num1.grid(row=0,column=0,padx=10,pady=10)
        self.ent_num1.grid(row=0,column=1,padx=10,pady=10)
        self.lbl_num2.grid(row=1,column=0,padx=10,pady=10)
        self.ent_num2.grid(row=1,column=1,padx=10,pady=10)
        self.lbl_num3.grid(row=2,column=0,padx=10,pady=10)
        self.ent_num3.grid(row=2,column=1,padx=10,pady=10)
        self.btn_active.grid(row=3,column=0,columnspan=2,pady=10)
    def management_events(self):
        """Maneja los eventos de la interfaz
        """
        pass
    def handler_errors(self,sem1,sem2,iteraciones):
        if not (isinstance(sem1, int) and isinstance(sem2, int) and isinstance(iteraciones, int)):
            raise ValueError("Todas las entradas deben ser números enteros.")
    def mostrar_error(self):
        messagebox.showerror("Error", "¡Ocurrió un error!")
    
    def show_table(self):
        try:
            sem1 = int(self.ent_num1.get())
            sem2 = int(self.ent_num2.get())
            iteraciones = int(self.ent_num3.get())
            # Verifica si las entradas son numéricas
            # self.handler_error(sem1, sem2, iteraciones)
            
            config.data = productos_medios(sem1, sem2, iteraciones)
            self.create_table(self.window, config.fields, config.data)
        except ValueError as e:
            # Muestra un mensaje de error si se ingresan valores no numéricos
            self.mostrar_error()
            print(e)
    
    def run_app(self):
        self.management_layout()
        self.window.mainloop()
        
class GreetingFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()
        
        self.greet_button = ttk.Button(
            self, text="Saludar", command=self.say_hello)
        self.greet_button.pack()
        
        self.greet_label = ttk.Label(self)
        self.greet_label.pack()
    
    def say_hello(self):
        self.greet_label["text"] = \
            "¡Hola, {}!".format(self.name_entry.get())
class AboutFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Visitanos en recursospython.com y "
                "foro.recursospython.com.")
        self.label.pack()
        
        self.web_button = ttk.Button(self, text="Visitar web")
        self.web_button.pack(pady=10)
        
        self.forum_button = ttk.Button(self, text="Visitar foro")
        self.forum_button.pack()
        
        
        
        
        
        
        
        
        # INICIAR LA APLICACIÓN
        
        
        
generator = App()
generator.run_app()