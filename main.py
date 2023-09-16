
import tkinter as tk
from tkinter import ttk,font
from config import config
from tkinter import messagebox
from methods import productos_medios, cuadrados_medios

class CuadradosMedios(ttk.Frame):
    def __init__(self,notebook):
        self.config = config
        self.frame_main = tk.Frame(notebook)
        self.init_section()
    def create_labels(self):
        """Crea los labels de la interfaz"""
        self.lbl_num1=tk.Label(self.frame_main, text="Semilla1: ")
        self.lbl_num3=tk.Label(self.frame_main, text="Iteraciones: ")
    def create_entries(self):
        """Crea los entries de la interfaz"""
        self.ent_num1=tk.Entry(self.frame_main)
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
            try:
                ttt=list(row[4])[0]
            except IndexError:
                ttt=None
            if ttt=="-":
                tree.insert("", "end", values=row,tags=("repeat",))
            elif i % 2 == 0:
                tree.insert("", "end", values=row,tags=("odd",))
            else: 
                tree.insert("", "end", values=row)
        # Mostrar la tabla
        tree.grid(row=50,column=0,columnspan=5,pady=40,padx=10)
    def management_layout(self):
        """Maneja el diseño de la interfaz
        """
        self.frame_main.grid(row=0,column=0,padx=10,pady=10)
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.lbl_num1.grid(row=0,column=0,padx=10,pady=10)
        self.ent_num1.grid(row=0,column=1,padx=10,pady=10)
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
            iteraciones = int(self.ent_num3.get())
            # Verifica si las entradas son numéricas
            # self.handler_error(sem1, sem2, iteraciones)
            
            config.data = cuadrados_medios(sem1, iteraciones)
            self.create_table(self.frame_main, config.fields_cm, config.data)
        except ValueError as e:
            # Muestra un mensaje de error si se ingresan valores no numéricos
            self.mostrar_error()
            print(f"Error: {e}")
    def init_section(self):
        self.management_layout()
        self.management_events()
class ProductosMedios:
    def __init__(self,notebook):
        self.config = config
        self.frame_main = tk.Frame(notebook)
        self.init_section()
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
            try:
                ttt=list(row[5])[0]
            except IndexError:
                ttt=None
            if ttt=="-":
                tree.insert("", "end", values=row,tags=("repeat",))
            elif i % 2 == 0:
                tree.insert("", "end", values=row,tags=("odd",))
            else: 
                tree.insert("", "end", values=row)
        # Mostrar la tabla
        tree.grid(row=50,column=0,columnspan=5,pady=40,padx=10)
    def management_layout(self):
        """Maneja el diseño de la interfaz
        """
        self.frame_main.grid(row=0,column=0,padx=10,pady=10)
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
            self.create_table(self.frame_main, config.fields, config.data)
        except ValueError as e:
            # Muestra un mensaje de error si se ingresan valores no numéricos
            self.mostrar_error()
            print(f"Error: {e}")
    def init_section(self):
        self.management_layout()
        self.management_events()
class App:
    def __init__(self):
        self.window = tk.Tk()
        self.config = config
        self.window.geometry(self.config.size)
        self.window.title(self.config.title)
        self.frame_main = tk.Frame(self.window)
        self.notebook = ttk.Notebook(self.window,style='lefttab.TNotebook',width=1000,height=800)
        
        self.style_notebook = ttk.Style()
        self.style_notebook.configure('lefttab.TNotebook', tabposition='wn')
        self.add_tabs()
        self.setup_fonts()
        self.set_styles()
        self.center_window(self.window,1000,800)
    def add_tabs(self):
        self.greeting_frame = CuadradosMedios(self.notebook)
        self.notebook.add(self.greeting_frame.frame_main, text="Saludos")
        self.about_frame = ProductosMedios(self.notebook)
        self.notebook.add(self.about_frame.frame_main, text="Productos Medios")
        self.notebook.grid(row=0,column=0)
        
    def setup_fonts(self):
        self.font_style = font.Font(weight="bold", family="Arial")
        self.window.option_add("*Font", self.font_style)
        
    def set_styles(self):
        ttk.Style().configure("Treeview", relief="flat",background="#00a7c7",foreground="white",font=('calibri', 11, 'bold'))
        style_btn = ttk.Style()
        style_btn.theme_use('alt')
        style_btn.configure('TButton', background = '#005585', foreground = 'white',borderwidth=1, focusthickness=3, focuscolor='none',font=('calibri', 11, 'bold'),width=20,height=4,anchor=tk.CENTER, padding=6)
        style_btn.map('TButton', background=[('active','#00a7c7')])
    def center_window(self,window, width, height):
        # Obtener las dimensiones de la pantalla
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        # Calcular las coordenadas x e y para centrar la ventana
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        # Establecer las coordenadas para centrar la ventana
        window.geometry(f"{width}x{height}+{x}+{y}")
    def run_app(self):
        self.window.mainloop()
        
        
app = App()
app.run_app()