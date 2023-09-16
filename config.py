from tkinter import ttk
class Config:
    def __init__(self):
        self.size = "1000x800"
        self.title = "Generador de Numeros Pseudoaleatorios"
        self.fields = ["n","x0","x00","x0*x00","largo","centro","ri"]
        self.fields_cm = ["n","x0","x0^2","largo","centro","ri"]
        self.data = [
                (0,0,0,0,0,0,0)
            ]
        # self.create_styles()
    def create_styles(self):
        self.styles_config = {         
                "TNotebook": {
                    "configure": {
                        "tabmargins": [0, 0, 0, 0],
                        "tabposition":'wn',
                        "background": "gray",
                    } 
                }, 

                "TNotebook.Tab": {
                    "configure": {
                        "padding": [12, 8],
                        "background": "lightgray",
                        "width" :22,
                        "foreground":"black"
                    },
                    "map": {
                        "background": [("selected", "lightblue"),("active", "white")],
                        "expand": [("selected", [1, 1, 1, 0])] ,
                    },
                },
                "Treeview.Heading":{
                    "configure": {
                        "background":"blue",
                        "font" : ('calibri', 13, 'bold'),
                        "foreground": "black",
                        
                        
                    }
                },
                "Treeview":{
                    "configure": {
                        "background":"lightgray",
                        "foreground": "black",
                        "font": ("calibri",11,"bold"),
                        "fieldbackground ":"black"
                    }
                }
        }
        self.styles = ttk.Style()
        #Si existe el estilo da error y lo modifica o actualiza.
        try:
            self.styles.theme_create( "MyStyle", parent="alt", settings= self.styles_config)
        except Exception as e:
            #Actualiza el fondo que tiene
            self.styles.theme_settings( "MyStyle", settings= self.styles_config)
            
        self.styles.theme_use("MyStyle")
        
# singleton
config = Config()
